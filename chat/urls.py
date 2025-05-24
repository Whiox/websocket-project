from django.urls import path
from chat.views import CreateChatView, ChatRoomView

urlpatterns = [
    path('chat/create/', CreateChatView.as_view(), name='create_chat'),
    path('chat/view/<int:room_id>/', ChatRoomView.as_view(), name='chat_room'),
]
