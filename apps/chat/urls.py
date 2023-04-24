from django.urls import path
from .views import *


urlpatterns = [
    path('send/message/<int:pk>/',SendMessageApiView.as_view()),
    path('new/contact/',ChatRoomApiView.as_view()),
    path('contact/delete/<int:pk>/',ChatRoomDeleteApiView.as_view()),
    path('contacts/',ListOfContacts.as_view()),
    path('message/<int:pk>/',MessageDetailApiView.as_view()),
    path('contacts/for/confirmation/',ContactUnderConsiderationApiView.as_view()),
    path('contact/confirm/<int:pk>/',ContactToConfirmApiView.as_view())

]