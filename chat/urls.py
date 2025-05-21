from django.urls import path
from chat.views import chat_room, CreateChatView

urlpatterns = [
    path('chat/create/', CreateChatView.as_view(), name='create_chat'),
    path('chat/view/<int:room_id>/', chat_room, name='chat_room'),
]
