from django.urls import path
from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSets
from chat.views import sumNumbersView

router = DefaultRouter()
router.register("chatroom", ChatRoomViewSets, basename="chatroom")
router.register("message", ChatRoomViewSets, basename="message")
urlpatterns = router.urls

urlpatterns += [
    path('sum_numbers/', sumNumbersView, name='sum_numbers'),
]