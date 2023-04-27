from django.db.models import Q
from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Follower
from .serializers import FollowSerializer


class FollowApiView(generics.CreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        to_user = request.data['to_user']
        if int(to_user) == request.user.pk:
            return Response({'ERROR':'You can not follow yourself'})
        return super().create(request, *args, **kwargs)
    

class FollowsApiView(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user = User.objects.get(id=pk)
        return Follower.objects.filter(from_user=user)
    

class RecommendationApiView(generics.ListAPIView):
    serializer_class = FollowSerializer
    queryset = Follower.objects.all()

    def get_queryset(self):
        recommedation = []
        user = self.request.user
        follows = Follower.objects.filter(from_user=user)
        for i in follows:
            if i.to_user != user:
                recommedation.append(i.to_user.id)

        return Follower.objects.filter(from_user__pk__in=recommedation).exclude(Q(from_user=user) | Q(to_user=user))
    


class FollowersApiView(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user = User.objects.get(id=pk)
        return Follower.objects.filter(to_user=user)
    


class UnfollowApiView(generics.RetrieveDestroyAPIView):
    serializer_class = FollowSerializer
    queryset = Follower.objects.all()

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        follower = Follower.objects.get(id=pk)
        if follower.from_user == request.user:
            return super().destroy(request, *args, **kwargs)
        return Response({'error':'this user is not followed'})
    

class DeleteFollowerApiView(generics.RetrieveDestroyAPIView):
    serializer_class = FollowSerializer
    queryset = Follower.objects.all()

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        follower = Follower.objects.get(id=pk)
        print(follower.from_user)
        if follower.to_user == request.user:
            return super().destroy(request, *args, **kwargs)
        return Response({'error':'This user is not your follower'})

      


