from django import forms
from chat.models import Chat


class CreateChatForm(forms.Form):
    name = forms.CharField(
        label="Название чата",
        max_length=100,
        widget=forms.TextInput(attrs={
            "placeholder": "Логин",
            "class": "form-input"
        })
    )

    def get_chat(self):
        chat_name = self.cleaned_data['name']

        return Chat.objects.create(name=chat_name)
