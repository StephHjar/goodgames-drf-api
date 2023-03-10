from rest_framework import serializers
from .models import Post
from likes.models import Like


class PostSerializer(serializers.ModelSerializer):
    """
    Post serializer. Code adapted from Code Institute's DRF API
    walkthrough.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    game_title = serializers.ReadOnlyField(source='game.title')
    game_image = serializers.ReadOnlyField(source='game.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, post=obj
            ).first()
            return like.id if like else None
        return None

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'game', 'created_at', 'updated_at', 'is_owner',
            'profile_id', 'profile_image', 'game_title', 'game_image',
            'currently_playing', 'completed', 'content', 'like_id',
            'comments_count', 'likes_count'
        ]
