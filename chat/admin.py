from django.contrib import admin
from chat.models import ChatRoom, Message

# Register your models here.
admin.site.register(Message)
admin.site.register(ChatRoom)
