from rest_framework import serializers

from apps.post.models import Post, PostImage,PostsLike,PostTag,PostVideo

class PostLikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PostsLike
        fields = '__all__'
        read_only_fields = ('id', 'user',)
        


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = "__all__"

class PostVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model= PostVideo
        fields = "__all__"

class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ['image']


class PostSerializer(serializers.ModelSerializer):
    post_images = PostImagesSerializer(many=True, read_only=True)
    post_video = PostVideoSerializer(many=True, read_only=True)
    list_of_likes = PostLikeSerializers(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id',
                  'title',
                  'description',
                  'user',
                  "tags",
                  'post_images',
                  'post_video',
                  'list_of_likes',
                  )

        read_only_fields = ('id', 'user', 'create_at')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["like's count"] = instance.list_of_likes.count()

        return representation


class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model=PostTag
        fields='__all__'
        read_only_fields = ('id', 'user',)