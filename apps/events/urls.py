from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(
    prefix="your",
    viewset=OwnEventsApiViewSet
)

router.register(
    prefix="events",
    viewset=EventApiViewSet
)

urlpatterns = router.urls
