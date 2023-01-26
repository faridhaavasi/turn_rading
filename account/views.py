from django.shortcuts import render
from django.views.generic import View
# Create your views here.

class user_login(View):
    def get(self, request):
        pass


def login(request):
    return render(request, 'account/login.html', {})