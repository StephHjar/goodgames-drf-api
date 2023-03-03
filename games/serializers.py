from rest_framework import serializers
from .models import Game
from likes.models import Like


class GameSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    like_id = serializers.SerializerMethodField()
    reviews_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

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

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(owner=user, game=obj).first()
            return like.id if like else None
        return None

    class Meta:
        model = Game
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'image',
            'description', 'like_id', 'reviews_count', 'likes_count'
        ]
