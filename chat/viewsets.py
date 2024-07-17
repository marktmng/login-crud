from django.contrib.auth.models import User
from rest_framework import viewsets

from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer, UserSerializer


class ChatRoomViewSets(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    
class MessageViewSets(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer