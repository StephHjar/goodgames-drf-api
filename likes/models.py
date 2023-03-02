from django.db import models
from django.contrib.auth.models import User
from posts.models import Post
from comments.models import Comment
from reviews.models import Review
from games.models import Game


class Like(models.Model):
    """
    Comment model, related to User, Comment, Post, and Game.
    Code from Code Institute's Django REST Framework walkthrough.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.OneToOneField(
        Post, related_name='likes', blank=True, null=True,
        on_delete=models.CASCADE
        )
    comment = models.OneToOneField(
        Comment, related_name='likes', blank=True, null=True,
        on_delete=models.CASCADE
    )
    review = models.OneToOneField(
        Review, related_name='likes', blank=True, null=True,
        on_delete=models.CASCADE
        )
    game = models.OneToOneField(
        Game, related_name='likes', blank=True, null=True,
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = [
            ['owner', 'post'], ['owner', 'comment'], ['owner', 'review'],
            ['owner', 'game'],
            ]

    def __str__(self):
        return f"{self.owner} {self.id}"
