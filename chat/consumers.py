import json
from channels.generic.websocket import AsyncWebsocketConsumer


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_name = f"chat_{self.room_id}"

        await self.channel_layer.group_add(self.room_name, self.channel_name)
        await self.accept()

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': f'{self.user} присоединился',
            }
        )

    async def disconnect(self, close_code):
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': f'{self.user} вышел',
            }
        )

        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')

        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
