from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from likes.models import Like


class Game(models.Model):
    """
    Game model, related to 'owner' i.e. a User instance.
    Code adapted from Code Institute's Django REST Framework walkthrough.
    """
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to='images/', default='../default_game_a6ytea', blank=True
    )
    description = models.TextField(blank=True)
    likes = GenericRelation(Like)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
