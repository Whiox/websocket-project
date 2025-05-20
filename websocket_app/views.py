from django.shortcuts import render

def chat_room(request, room_name):
    """
    Отображает страницу чата для заданной комнаты.
    :param room_name: имя комнаты (из URL)
    """
    return render(request, 'chat.html', {
        'room_name': room_name
    })
