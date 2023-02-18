from django.contrib.auth.models import User
from .models import Post
from games.models import Game
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    """
    Tests adapted from Code Institute's Django REST Framework walkthrough.
    """
    def setUp(self):
        User.objects.create_user(username='steph', password='test')
        Game.objects.create(title='test game')

    def test_can_list_posts(self):
        steph = User.objects.get(username='steph')
        Post.objects.create(owner=steph, game_id=1)
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_post(self):
        self.client.login(username='steph', password='test')
        response = self.client.post('/posts/', {'game': 1})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'game': 1})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
