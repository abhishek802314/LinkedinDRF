from rest_framework import serializers 
from .models import Follower

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id', 'from_user', 'to_user', 'create_at']
        read_only_fields = ('from_user', )