from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


from .models import User, Post, Comment, Like, Follow

def unfollow(request, username):
    follower = User.objects.get(username=username)
    following = request.user
    follow = Follow.objects.filter(follower=follower, following=following)
    follow.delete()
    return JsonResponse({"message": "User succesfully unfollowed!"})

def follow(request, username):
    follower = User.objects.get(username=username)
    following = request.user
    new_follow = Follow(
        follower=follower,
        following=following
    )
    new_follow.save()
    return JsonResponse({"message": "User succesfully followed!"})


def unlike(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = request.user
    like = Like.objects.filter(user=user, post=post)
    like.delete()
    return JsonResponse({"message": "Like remove!"})

def like(request, post_id):
    post = Post.objects.get(pk=post_id)
    user = request.user
    new_like = Like(user=user, post=post)
    new_like.save()
    return JsonResponse({"message": "Like added!"})

def comment(request, id):
    comment_form = request.POST.get("post-comment")
    post = Post.objects.get(pk=id)
    if comment_form:
        new_comment = Comment(
            author = request.user,
            content = comment_form,
            post = post
        )
        new_comment.save()
        return redirect(reverse('post', kwargs={'id': id}))

def profile(request, username):
    user = User.objects.get(username=username)
    posts = Post.objects.filter(user=user).order_by('-date')
    page_obj = paginator(request, posts, 10)


    if request.user.is_authenticated:
        login_user = request.user
        liked = set(Like.objects.filter(user=request.user).values_list('post_id', flat=True))
        followed= set(User.objects.filter(followers__following=request.user))
        print(followed)
    else:
        liked = []
        followed = []


    return render(request, "network/profile.html", {
        "posts": page_obj,
        "username": username,
        "page_obj": page_obj,
        "liked": liked,
        "followed": followed,
        "login_user": login_user
    })

def paginator(request, posts, number):
    p = Paginator(posts, number)
    page_num = request.GET.get('page')
    page_obj = p.get_page(page_num)
    return page_obj

def index(request):
    posts = Post.objects.order_by('-date')
    page_obj = paginator(request, posts, 10)

    if request.user.is_authenticated:
        liked = set(Like.objects.filter(user=request.user).values_list('post_id', flat=True))
    else:
        liked = []

    if request.method == "POST":
        post_form = request.POST.get("post-text")

        if post_form:
            new_post = Post(
                user=request.user,
                content = post_form
            )
            new_post.save()
            return redirect('index')
    return render(request, "network/index.html", {
        "posts": page_obj,
        "page_obj": page_obj,
        "liked": liked
    })
        

def post(request, id):
    post = get_object_or_404(Post, id=id)
    comments = Comment.objects.filter(post=post).order_by("-date")

    if request.user.is_authenticated:
        liked = set(Like.objects.filter(user=request.user).values_list('post_id', flat=True))
    else:
        liked = []


    if request.method == "POST":
        if 'post-comment' in request.POST:
            return comment(request, id=id)
    return render(request, "network/singlepost.html", {
        "post": post,
        "comments": comments,
        "liked": liked
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
