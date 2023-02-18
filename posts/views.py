from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from goodgames_drf_api.permissions import IsOwnerOrReadOnly


class PostList(APIView):
    serializer_class = PostSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(
            posts, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


# class GameDetail(APIView):
#     serializer_class = GameSerializer
#     permission_classes = [IsOwnerOrReadOnly]

#     def get_object(self, pk):
#         try:
#             game = Game.objects.get(pk=pk)
#             self.check_object_permissions(self.request, game)
#             return game
#         except Game.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         game = self.get_object(pk)
#         serializer = GameSerializer(
#             game, context={'request': request}
#         )
#         return Response(serializer.data)

#     def put(self, request, pk):
#         game = self.get_object(pk)
#         serializer = GameSerializer(
#             game, data=request.data, context={'request': request}
#         )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(
#             serializer.errors, status=status.HTTP_400_BAD_REQUEST
#             )

#     def delete(self, request, pk):
#         game = self.get_object(pk)
#         game.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )
