from django.utils import timezone
from django.contrib.auth import get_user_model

from rest_framework import viewsets,permissions,filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from apps.post.serializers import PostSerializer,PostImageSerializer,PostLikeSerializers,PostTagSerializer,PostVideoSerializer
from apps.post.models import Post,PostImage,PostsLike,PostTag,PostVideo
from apps.post.permissions import IsPostOwner
from apps.user.permissions import IsOwner

User=get_user_model()



class PostApiViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['title','tags']

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)



class PostTagApiViewSet(viewsets.ModelViewSet):
    
    queryset=PostTag.objects.all()
    serializer_class=PostTagSerializer
    permission_classes=[IsOwner]
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['title']

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user) 

    def get_queryset(self):
        return PostTag.objects.filter(user=self.request.user)


class PostImageApiViewSet(viewsets.ModelViewSet):

    queryset = PostImage.objects.all()
    serializer_class = PostImageSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy',]:
            return (IsPostOwner(), )
        else:
            return (permissions.IsAuthenticated(),)  


    def create(self, request, *args, **kwargs):
        post = request.data['post']
        owner=Post.objects.get(id=post).user
        user = request.user
        if user==owner:
            return super().create(request,*args, **kwargs)
        return Response({"ERROR":"You cannot add an image, you are not the owner of this post"})


class PostVideoApiViewSet(viewsets.ModelViewSet):

    queryset = PostVideo.objects.all()
    serializer_class = PostVideoSerializer

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy',]:
            return (IsPostOwner(), )
        else:
            return (permissions.IsAuthenticated(),)  


    def create(self, request, *args, **kwargs):
        post = request.data['post']
        owner=Post.objects.get(id=post).user
        user = request.user
        if user==owner:
            return super().create(request,*args, **kwargs)
        return Response({"ERROR":"You cannot add an video, you are not the owner of this post"})





class PostLikeApiView(viewsets.ModelViewSet):

    queryset=PostsLike.objects.all()
    serializer_class=PostLikeSerializers
    

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)


    def create(self, request, *args, **kwargs):

        post = request.data['post']
        user=request.user       
        if  PostsLike.objects.filter(post_id=post,user=user):
            return Response({"error":"you can't like twice"})
        return super().create(request,*args, **kwargs)



    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)