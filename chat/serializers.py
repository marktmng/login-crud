from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import ChatRoom

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id', 'name', 'members', 'created_by']
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['text', 'chat_room', 'user']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']