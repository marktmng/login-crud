from rest_framework.routers import DefaultRouter
from chat.viewsets import ChatRoomViewSets

router = DefaultRouter()
router.register("chatroom", ChatRoomViewSets, basename="chatroom")
router.register("message", ChatRoomViewSets, basename="message")
urlpatterns = router.urls