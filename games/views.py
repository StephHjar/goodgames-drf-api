from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Game
from .serializers import GameSerializer


class GameList(APIView):
    def get(self, request):
        games = Game.objects.all()
        serializer = GameSerializer(
            games, many=True, context={'request': request}
        )
        return Response(serializer.data)
