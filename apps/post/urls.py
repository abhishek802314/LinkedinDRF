from rest_framework.routers import DefaultRouter
from django.urls import path

from .views import *


router = DefaultRouter()


router.register(prefix='post',viewset=PostApiViewSet)
router.register(prefix='image',viewset=PostImageApiViewSet)
router.register(prefix='video',viewset=PostVideoApiViewSet)
router.register(prefix='like',viewset=PostLikeApiView)
router.register(prefix='tags', viewset=PostTagApiViewSet)



urlpatterns = router.urls