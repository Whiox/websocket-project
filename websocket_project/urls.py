from django.contrib import admin
from django.urls import path
from websocket_app.views import chat_room

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/<str:room_name>/', chat_room, name='chat_room'),
]
