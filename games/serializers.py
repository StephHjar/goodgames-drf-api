from rest_framework import serializers
from .models import Game


class GameSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

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

    class Meta:
        model = Game
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'title', 'image',
            'description'
        ]
