from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(
    prefix='',
    viewset=CommentApiViewSet
)

router.register(
    prefix='like',
    viewset=CommentLikeApiView
)

urlpatterns = router.urls