from django.db import models
from django.contrib.auth.models import User
from games.models import Game


class Post(models.Model):
    """
    Post model, related to 'owner' i.e. a User instance, and to 'game' i.e. a
    Game instance.
    Code adapted from Code Institute's Django REST Framework walkthrough.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    currently_playing = models.BooleanField(default=True, blank=True,
                                            null=True)
    completed = models.BooleanField(default=False, blank=True, null=True)
    content = models.TextField(blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.game.title} {self.owner}'
