from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.response import Response

from apps.user.serializers import UserSerializer
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer, ContactUnderConsiderationSerializer
from .permissions import IsSender, IsReceiver


class ChatRoomApiView(generics.CreateAPIView):
    '''for creating chat rooms'''
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)
    


class ChatRoomDeleteApiView(generics.DestroyAPIView):
    '''for deleting chat rooms'''
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [IsSender]



class ContactUnderConsiderationApiView(generics.ListAPIView):
    ''' contact requests '''
    queryset = ChatRoom.objects.all()
    serializer_class = ContactUnderConsiderationSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return ChatRoom.objects.filter(receiver=self.request.user, is_contact=False)
    

class ContactToConfirmApiView(generics.RetrieveUpdateAPIView):
    '''for confirm contact requests '''
    queryset = ChatRoom.objects.all()
    serializer_class = ContactUnderConsiderationSerializer
    permission_classes = [IsReceiver]


    def get_queryset(self):
        return ChatRoom.objects.filter(receiver=self.request.user, is_contact=False)
    

class SendMessageApiView(generics.ListCreateAPIView):
    ''' To send and receive private messages '''
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


    def get(self, request, pk):
        chat_room = ChatRoom.objects.get(id=pk)
        if request.user==chat_room.sender and chat_room.is_contact==True or request.user==chat_room.receiver and chat_room.is_contact==True:
            messages = Message.objects.filter(chat_room=chat_room)
            serializer=MessageSerializer(messages, many=True)
            return Response(serializer.data)
        else:
            return Response({'Error':'You dont have this chat'})
        
    
    def create(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        chat_room = ChatRoom.objects.get(id=pk)
        if chat_room.is_contact==True:
            if request.user==chat_room.sender or request.user==chat_room.receiver:
                return super().create(request, *args, **kwargs)
            return Response({'Error':'You can not send message as its not your contact'})
        return Response({'Error':'Under Consideration'})
    

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        receiver = ChatRoom.objects.get(id=pk).receiver
        sender = self.request.user
        if receiver==sender:
            return serializer.save(chat_room=ChatRoom.objects.get(id=pk), receiver=ChatRoom.objects.get(id=pk), sender=sender)
        
        return serializer.save(chat_room=ChatRoom.objects.get(id=pk),receiver=receiver,sender=sender)
    


class MessageDetailApiView(generics.RetrieveUpdateAPIView):
    ''' to delete and update messages'''
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsSender]



class ListOfContacts(generics.ListAPIView):
    '''your all contact list'''
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        return ChatRoom.objects.filter(Q(sender=self.request.user, is_contact=True)|Q(receiver=self.request.user, is_contact=True))
    
   