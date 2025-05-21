from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from chat.models import Chat


def chat_room(request, room_id):
    chat = get_object_or_404(Chat, id=room_id)

    context = {
        'room_id': chat.id,
        'room_name': chat.name
    }

    return render(request, 'chat.html', context)


class CreateChatView(View):
    @staticmethod
    def get(request):
        chat = Chat.objects.create(name='not now')
        return redirect('chat_room', chat.id)
