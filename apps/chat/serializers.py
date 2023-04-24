from rest_framework import serializers
from .models import ChatRoom, Message



class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'receiver', 'sender']
        read_only_fields = ('sender', )


class ContactUnderConsiderationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'receiver', 'sender', 'is_contact']
        read_only_fields = ('id', 'sender', 'receiver')


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id', 'timestamp', 'chat_room', 'sender', 'receiver',)
