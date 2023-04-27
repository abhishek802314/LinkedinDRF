from django.urls import path
from .views import *


urlpatterns = [
    path('follow/',FollowApiView.as_view()),
    path('user/<int:pk>/follows/',FollowsApiView.as_view()),
    path('user/<int:pk>/followers/',FollowersApiView.as_view()),
    path('unfollow/<int:pk>/',UnfollowApiView.as_view()),
    path('delete/follower/<int:pk>/',DeleteFollowerApiView.as_view()),
    path('recommendations/',RecommendationApiView.as_view()),

]