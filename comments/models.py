from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from posts.models import Post
from likes.models import Like


class Comment(models.Model):
    """
    Comment model, related to User and Post.
    Code from Code Institute's Django REST Framework walkthrough.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    likes = GenericRelation(Like)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
