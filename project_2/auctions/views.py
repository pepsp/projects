from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.db.models import Max
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import *
from django.http import JsonResponse
from django import forms


class NewListingForm(forms.Form):
    title = forms.CharField(label="Title:", widget=forms.TextInput(attrs={'placeholder': "Enter item name"}))
    description = forms.CharField(label="Item's description:", widget=forms.TextInput(attrs={'placeholder': "Enter an item description"}))
    image_url= forms.CharField(label="Image URL:", widget=forms.TextInput(attrs={"placeholder": "Enter image URL"}))
    category = forms.ModelChoiceField(label="Choose a Category", queryset=Category.objects.all(), initial=9, required=True)
    owner = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    base_price = forms.DecimalField(label="Enter price:", widget=forms.TextInput(attrs={'placeholder': '00.00$'}))

class NewCommentForm(forms.Form):
    comment = forms.CharField(label="", widget=forms.Textarea(attrs={'placeholder': 'Enter your comment', 'class': 'form-control', 'rows': '3'}))

class NewBidForm(forms.Form):
    bid = forms.DecimalField(label="Enter bid:", widget=forms.TextInput(attrs={'placeholder': '00.00$'}))

def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")
    

@login_required
def new(request):
    if request.method == "POST":
        form = NewListingForm(request.POST)
        if form.is_valid():
            new_listing = Listing(
                title = form.cleaned_data["title"],
                description = form.cleaned_data["description"],
                base_price = form.cleaned_data["base_price"],
                image_url = form.cleaned_data["image_url"],
                category = form.cleaned_data["category"],
                owner = request.user
            )
            new_listing.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/create_listing.html", {"form": form})

    else:
        return render(request, "auctions/create_listing.html", {
                "form": NewListingForm()
                    })


def categories(request):
    return render(request, "auctions/categories.html")

@login_required
def watchlist(request):
    return render(request, "auctions/watchlist.html")

def item(request, id):
    listing = get_object_or_404(Listing, pk=id)
    comments = Comment.objects.filter(listing=listing)
    bids = Bid.objects.filter(listing=listing)
    highest_bid = Bid.objects.filter(listing=listing).aggregate(Max('bid'))['bid__max']
    bids_count = bids.count()  # Count the number of bids

    if request.method == "POST": 
        if 'submit-comment' in request.POST:
            comment_form = NewCommentForm(request.POST)
            if comment_form.is_valid():
                new_comment = Comment(
                    listing = listing,
                    author = request.user,
                    comment = comment_form.cleaned_data["comment"]
                    )
                new_comment.save()
                return redirect('item', id=id)
            
        if 'submit-bid' in request.POST:
            bid_form = NewBidForm(request.POST)
            if bid_form.is_valid():
                new_bid_amount = bid_form.cleaned_data["bid"]
                if new_bid_amount > listing.base_price and (not highest_bid or new_bid_amount > highest_bid):
                    new_bid = Bid(
                        listing = listing,
                        user = request.user,
                        bid = bid_form.cleaned_data["bid"]
                    )
                    new_bid.save()
                    return redirect("item", id=id)
                else:
                    error_message = "Bid amount is too low!"
                return render(request, "auctions/error.html", {"error_message": error_message})
                
        elif 'submit-sell' in request.POST:
            pass
        elif 'submit-watchlist' in request.POST:
            pass
    
    comment_form = NewCommentForm()
    bid_form = NewBidForm()

    return render(request, "auctions/item.html", {
        "listing": listing,
        "comments": comments,
        "user": request.user,
        "comment_form": comment_form,
        "bid_form": bid_form,
        "highest_bid": highest_bid,
        "bids": bids,
        "bids_count": bids_count

    } )

@login_required
def myindex(request):
    active_listings = Listing.objects.filter(owner=request.user, is_active=True)
    finished_listings = Listing.objects.filter(owner=request.user, is_active=False)
    return render(request, "auctions/myindex.html", {
        "active_listings": active_listings,
        "finished_listings": finished_listings
    })

def end(request):
    pass

def bid(request):
    pass

