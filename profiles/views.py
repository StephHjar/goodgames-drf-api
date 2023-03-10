from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from goodgames_drf_api.permissions import IsOwnerOrReadOnly


class ProfileList(generics.ListAPIView):
    """
    List all profiles. Code adapted from Code Institute's DRF API
    walkthrough.
    """
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        reviews_count=Count('owner__review', distinct=True),
    ).order_by('-created_at')
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.OrderingFilter
    ]
    ordering_fields = ['posts_count']


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Update and destroy profiles. Code adapted from Code Institute's DRF API
    walkthrough.
    """
    serializer_class = ProfileSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.annotate(
        posts_count=Count('owner__post', distinct=True),
        reviews_count=Count('owner__review', distinct=True),
    ).order_by('-created_at')
