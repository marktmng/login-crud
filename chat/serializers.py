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