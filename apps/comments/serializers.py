from rest_framework import serializers
from .models import Comment, CommentLike



class CommentLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentLike
        fields = '__all__'
        read_only_fields = ('id', 'user', )



class CommentSerializer(serializers.ModelSerializer):
    comment_for_like = CommentLikeSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['comment', 'post', 'user', 'create_at', 'parent', 'comment_for_like']
        read_only_fields = ['id', 'user', 'create_at']


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["like's count"] = instance.comment_for_like.count()
        return representation
    
