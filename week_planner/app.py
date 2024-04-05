from flask import Flask, render_template, request, redirect
from cs50 import SQL

app = Flask(__name__)
db = SQL("sqlite:///week.db")

@app.route("/")
def index():
    days, display_task, display_start = get_data()
    return render_template("index.html",days=days, tasks=display_task, starts=display_start)

@app.route("/edit", methods = ["GET", "POST"])
def edit():
    days, display_task, display_start = get_data()

    if request.method == "GET":
        return render_template("edit.html", days=days, tasks = display_task, starts = display_start)
    if request.method == "POST":
        day = request.form.getlist("day")
        start = request.form.get("start")
        task = request.form.get("task")

        if not day or not start or not task:
            return render_template("missing.html")

        for i in day:
            check_start = db.execute("SELECT COUNT(start) AS count from tasks WHERE start = ? AND day_id = ?", start, i)
            if check_start[0]["count"] ==1:
                db.execute("UPDATE tasks SET title = ? WHERE start = ? AND day_id = ?", task, start, i)

            else:
                db.execute("INSERT INTO tasks(day_id, start, title) VALUES(?,?,?)", i, start, task)
        return redirect("/edit")


@app.route("/clear", methods = ["GET"])
def clear():
    if request.method == "GET":
        db.execute("DELETE FROM tasks")
        return redirect("/")


def get_data():
    days = db.execute("SELECT * FROM days")
    display_task = db.execute("SELECT * FROM tasks ORDER BY start")
    display_start = db.execute("SELECT DISTINCT start FROM tasks ORDER BY start")
    return days, display_task, display_start


if __name__ == '__main__':
    app.run(debug=True)
