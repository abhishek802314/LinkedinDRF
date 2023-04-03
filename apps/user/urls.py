from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    prefix='user',
    viewset=UserApiView
)

router.register(
    prefix='education',
    viewset=EducationInformationApiView
)

router.register(
    prefix='skill',
    viewset=SkillsApiView
)

router.register(
    prefix='position',
    viewset=PositionApiView
)

router.register(
    prefix='premium',
    viewset=PremiumViewSet
)

urlpatterns = router.urls