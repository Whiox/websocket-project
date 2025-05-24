from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from chat.models import Chat

from chat.forms import CreateChatForm


class CreateChatView(View):
    @staticmethod
    @login_required
    def get(request):
        return render(request, 'create_chat.html', context = {'form': CreateChatForm})

    @staticmethod
    @login_required
    def post(request):
        form = CreateChatForm(request.POST)
        if form.is_valid():
            chat = form.get_chat()
            return redirect('chat_room', room_id=chat.id)
        return render(request, 'create_chat.html', context = {'form': form})


class ChatRoomView(View):
    @staticmethod
    @login_required
    def get(request, room_id):
        chat = get_object_or_404(Chat, id=room_id)

        context = {
            'room_id': chat.id,
            'room_name': chat.name
        }

        return render(request, 'chat.html', context)
