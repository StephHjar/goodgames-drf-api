from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Game
from .serializers import GameSerializer
from goodgames_drf_api.permissions import IsOwnerOrReadOnly


class GameList(generics.ListCreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Game.objects.annotate(
        reviews_count=Count('review', distinct=True),
        likes_count=Count('likes', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'title'
    ]
    ordering_fields = ['likes_count', 'reviews_count', 'likes__created_at']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Game.objects.annotate(
        likes_count=Count('likes', distinct=True),
        reviews_count=Count('review', distinct=True)
    ).order_by('-created_at')


class GameTitles(generics.ListAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = None
    queryset = Game.objects.all().order_by('title')
