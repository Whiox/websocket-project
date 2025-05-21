import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async

from chat.models import Chat, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']

        if self.user.is_anonymous:
            return await self.close(code=4001)

        self.chat_id = self.scope['url_route']['kwargs']['room_id']
        self.chat_name = f"chat_{self.chat_id}"

        await self.channel_layer.group_add(self.chat_name, self.channel_name)
        await self.accept()

        await self.channel_layer.group_send(
            self.chat_name,
            {
                'type': 'chat_message',
                'message': f'{self.user} присоединился',
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_send(
            self.chat_name,
            {
                'type': 'chat_message',
                'message': f'{self.user} вышел',
            }
        )

        await self.channel_layer.group_discard(
            self.chat_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')

        await self.save_message(self.user, message)

        await self.channel_layer.group_send(
            self.chat_name,
            {
                'type': 'chat_message',
                'sender': str(self.user),
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'sender': str(self.user),
            'message': message
        }))

    @database_sync_to_async
    def save_message(self, user, text):
        chat = Chat.objects.get(id=self.chat_id)
        return Message.objects.create(
            sender=user,
            chat=chat,
            text=text
        )
