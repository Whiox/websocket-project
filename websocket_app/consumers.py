import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # получаем название комнаты из URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # присоединяемся к группе
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        # принимаем соединение
        await self.accept()

    async def disconnect(self, close_code):
        # покидаем группу
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Получили сообщение от WebSocket (от клиента)
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')

        # рассылаем всем в группе
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',  # укажем handler
                'message': message
            }
        )

    # Handler для типа 'chat_message'
    async def chat_message(self, event):
        message = event['message']

        # отправляем сообщение обратно на WS
        await self.send(text_data=json.dumps({
            'message': message
        }))
