from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10, default='', allow_blank=True)
    rating = serializers.ChoiceField(choices=Movie.RATING_CHOICES, default='G')
    synopsis = serializers.CharField(default='', allow_blank=True)
    added_by = serializers.SerializerMethodField()
    
    def get_added_by(self, obj):
        return obj.user.email if obj.user else None

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    

