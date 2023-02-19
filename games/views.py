from rest_framework import generics, permissions
from .models import Game
from .serializers import GameSerializer
from goodgames_drf_api.permissions import IsOwnerOrReadOnly


class GameList(generics.ListCreateAPIView):
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Game.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Game.objects.all()
