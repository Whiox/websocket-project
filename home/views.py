from django.shortcuts import render
from django.views import View


class HomePageView(View):
    @staticmethod
    def get(request):
        return render(request, 'home.html')
