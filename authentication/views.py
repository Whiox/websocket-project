from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, RegisterForm
from authentication.models import User


class LoginView(View):
    @staticmethod
    def get(request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    @staticmethod
    def post(request):
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')
        return render(request, 'login.html', {'form': form})


class RegisterView(View):
    @staticmethod
    def get(request):
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})

    @staticmethod
    def post(request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('/')
        return render(request, 'register.html', {'form': form})


class LogoutView(View):
    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            logout(request)
        return redirect('')
