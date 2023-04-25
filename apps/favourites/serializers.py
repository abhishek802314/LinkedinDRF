from rest_framework import serializers
from .models import Favourite, FavouriteFolder


class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = ('folder', 'post', 'user',)
        read_only_fields = ('id', 'user', )

    

class FavouriteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavouriteFolder
        fields = ('id', 'title', 'user')
        read_only_fields = ('user', )