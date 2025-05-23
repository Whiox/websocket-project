from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from authentication.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Логин",
        max_length=150,
        widget=forms.TextInput(attrs={
            "placeholder": "Логин",
            "class": "form-input"
        })
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Пароль",
            "class": "form-input"
        })
    )


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Логин",
        max_length=150,
        widget=forms.TextInput(attrs={
            "placeholder": "Имя пользователя",
            "class": "form-input"
        })
    )
    name = forms.CharField(
        label="Имя",
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            "placeholder": "Отображаемое имя",
            "class": "form-input"
        })
    )
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Пароль",
            "class": "form-input"
        })
    )
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput(attrs={
            "placeholder": "Повторите пароль",
            "class": "form-input"
        })
    )

    class Meta:
        model = User
        fields = ("username", "name", "password1", "password2")
