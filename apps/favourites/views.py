from rest_framework import viewsets, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Favourite, FavouriteFolder
from .serializers import FavouriteSerializer, FavouriteCategorySerializer
from apps.user.permissions import IsOwner


class FavouriteCategoryApiViewSet(viewsets.ModelViewSet):
    # your own category(favourite)
    queryset =FavouriteFolder.objects.all()
    serializer_class = FavouriteCategorySerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title']
    permission_classes = [IsOwner,]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset()).filter(user=request.user)
        serializer = FavouriteCategorySerializer(queryset, many=True)
        return Response(serializer.data)
    

class FavouriteApiViewSet(viewsets.ModelViewSet):
    # your own favourites
    queryset = Favourite.objects.all()
    serializer_class = FavouriteSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['folder', 'post']
    permission_classes = [IsOwner]


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def list(self, requeust):
        queryset = self.filter_queryset(self.get_queryset()).filter(user=requeust.user)
        serializer = FavouriteSerializer(queryset, many=True)
        return Response(serializer.data)
    
    
        