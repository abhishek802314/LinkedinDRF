from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import FavouriteApiViewSet, FavouriteCategoryApiViewSet


router = DefaultRouter()

router.register(prefix='my', viewset=FavouriteApiViewSet),
router.register(prefix='category', viewset=FavouriteCategoryApiViewSet)
urlpatterns = router.urls

