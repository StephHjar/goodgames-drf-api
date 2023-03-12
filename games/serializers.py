from rest_framework import serializers
from .models import Game
from likes.models import Like
from reviews.models import Review


class GameSerializer(serializers.ModelSerializer):
    """
    Game model serializer. Code adapted from Code Institute's DRF API
    walkthrough.
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_admin = serializers.SerializerMethodField()
    like_id = serializers.SerializerMethodField()
    reviews_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()
    review_id = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096 px!'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096 px!'
            )
        return value

    def get_is_admin(self, obj):
        user = self.context['request'].user
        return user.username == 'admin'

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, game=obj).first()
            return like.id if like else None
        return None

    def get_review_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            review = Review.objects.filter(owner=user, game=obj).first()
            return review.id if review else None
        return None

    class Meta:
        model = Game
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'image',
            'description', 'like_id', 'reviews_count', 'likes_count',
            'is_admin', 'review_id',
        ]
