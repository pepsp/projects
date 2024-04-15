from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import *
from django import forms


class NewListingForm(forms.Form):
    title = forms.CharField(label="Title:", widget=forms.TextInput(attrs={'placeholder': "Enter item name"}))
    description = forms.CharField(label="Item's description:", widget=forms.TextInput(attrs={'placeholder': "Enter an item description"}))
    image_url= forms.CharField(label="Image URL:", widget=forms.TextInput(attrs={"placeholder": "Enter image URL"}))
    category = forms.ModelChoiceField(label="Choose a Category", queryset=Category.objects.all(), initial=9, required=True)
    owner = forms.IntegerField(widget=forms.HiddenInput(), required=False)
    base_price = forms.DecimalField(label="Enter price:", widget=forms.TextInput(attrs={'placeholder': '00.00$'}))

    
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


def watchlist(request):
    return render(request, "auctions/watchlist.html")
