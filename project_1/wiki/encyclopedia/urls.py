from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("random_entry", views.random_entry, name="random_entry"),
    path("edit", views.edit, name="edit"),
    path("save_edit", views.save_edit, name="save_edit")
]
