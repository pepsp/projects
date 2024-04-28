import os
from datetime import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    check_stock = db.execute("SELECT * FROM stocks WHERE user_id = ?", user_id)
    if not check_stock:
        return render_template("index.html", cash=0, total=0)
    else:
        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        rows = db.execute(
            "SELECT symbol, SUM(shares) AS shares, price, SUM(total) AS total FROM stocks WHERE user_id = ? GROUP BY symbol", user_id)
        total_stocks = db.execute(
            "SELECT SUM(total) AS total FROM stocks WHERE user_id = ?", user_id)
        total_sum = float(total_stocks[0]["total"]) + float(cash[0]["cash"])

        return render_template("index.html", datos=rows, cash=cash[0]["cash"], total=total_sum)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET":
        return render_template("buy.html")
    if request.method == "POST":
        shares = request.form.get("shares")
        if not shares.isdigit():
            return apology("only complete numbers allowed", 400)
        if not shares or int(shares) <= 0:
            return apology("invalid shares", 400)
        buySymbol = lookup(request.form.get("symbol"))
        if not buySymbol:
            return apology("missing symbol", 400)

        user_id = session["user_id"]
        price = buySymbol["price"]
        stock = buySymbol["symbol"]
        timestamp = datetime.now()

        total_price = float(price) * float(shares)
        user_cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        if int(user_cash[0]["cash"]) < total_price:
            return apology("not enough cash", 403)
        else:
            remaining_cash = int(user_cash[0]["cash"]) - total_price
            db.execute("INSERT INTO stocks (user_id, symbol, shares, price, timestamp,total) VALUES(?,?,?,?,?,?)",
                       user_id, stock, shares, price, timestamp, total_price)
            db.execute("UPDATE stocks SET symbol = UPPER(symbol)")
            db.execute("UPDATE users SET cash = ? wHERE id = ?", remaining_cash, user_id)

            flash(f"You bought {int(shares)} {stock} shares for {usd(total_price)}!")
            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    if request.method == "GET":
        user_id = session["user_id"]
        rows = db.execute("SELECT * FROM stocks WHERE user_id = ?", user_id)
        return render_template("history.html", datos=rows)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "GET":
        return render_template("quote.html")
    elif request.method == "POST":
        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("invalid symbol", 400)
        quote_price = quote["price"]
        quote_symbol = quote["symbol"]
        return render_template("quote_found.html", quote_price=quote_price, quote_symbol=quote_symbol)


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        check_username = db.execute(
            "SELECT COUNT(*) FROM users WHERE username = ?", request.form.get("username"))
        if check_username[0]["COUNT(*)"] == 1:
            return apology("user already exists", 400)

        if not request.form.get("username"):
            return apology("must provide username", 400)
        if not request.form.get("password"):
            return apology("must provide password", 400)
        if not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 400)

        db.execute("INSERT INTO users (username,hash) VALUES (?,?)", request.form.get(
            "username"), generate_password_hash(request.form.get("password")))
        login = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        session["user_id"] = login[0]["id"]
    return redirect("/")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    user_id = session["user_id"]
    """Sell shares of stock"""

    if request.method == "GET":
        option = db.execute("SELECT DISTINCT symbol FROM stocks WHERE user_id = ?", user_id)
        return render_template("sell.html", option=option)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        if not symbol:
            return apology("missing symbol", 400)
        shares = request.form.get("shares")
        owned_shares = db.execute(
            "SELECT SUM(shares) AS shares FROM stocks WHERE symbol = ? AND user_id = ?", symbol, user_id)
        if not shares.isdigit():
            return apology("only complete numbers allowed", 400)
        if not shares or int(shares) <= 0:
            return apology("invalid shares", 400)
        if int(shares) > int(owned_shares[0]["shares"]):
            return apology("not enough shares", 400)

        price = lookup(symbol)
        price = float(price["price"])
        profit = float("{:.2f}".format((price) * int(shares)))
        timestamp = datetime.now()

        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", profit, user_id)
        db.execute("INSERT INTO stocks (user_id, symbol, shares, price, timestamp,total) VALUES(?,?,?,?,?,?)",
                   user_id, symbol, -int(shares), price, timestamp, -profit)
        db.execute("UPDATE stocks SET symbol = UPPER(symbol)")
        flash(f"You sold {shares} {symbol} shares for {usd(price)}!")
        return redirect("/")


@app.route("/change", methods=["GET", "POST"])
def change():
    if request.method == "GET":
        return render_template("change.html")
    if request.method == "POST":
        username = request.form.get("username")
        verify_user = db.execute("SELECT COUNT(id) AS id FROM users WHERE username = ?", username)
        if verify_user[0]["id"] != 1:
            return apology("username not found", 400)
        old_pass = request.form.get("old")
        new_pass = request.form.get("new")
        if not old_pass:
            return apology("must provide old password")
        if not new_pass:
            return apology("must provide new password")

        new_pass = generate_password_hash(new_pass)
        verify_pass = db.execute("SELECT hash FROM users WHERE username = ?", username)
        verify_pass = verify_pass[0]["hash"]

        if check_password_hash(verify_pass, old_pass) == False:
            return apology("old password does not match", 400)
        elif check_password_hash(verify_pass, old_pass) == True:
            db.execute("UPDATE users SET hash = ? WHERE username = ?", new_pass, username)
            flash("You succesfully changed your password!")
            return redirect("/")
