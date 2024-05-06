from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="author_post")
    content = models.CharField(max_length=280)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Post {self.id} made by {self.user} on {self.date.strftime('%d %b %Y %H:%M:%S')}"

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="author_comment")
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name="post_comment")
