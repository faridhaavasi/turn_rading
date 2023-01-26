from django.shortcuts import render
from django.views.generic import View
from .forms import Login_Form
# Create your views here.

class user_login(View):
    def get(self, request):
        form = Login_Form() #instans is form
        return render(request, 'account/login.html', {'form':form})

'''
#test ok
def login(request):
    return render(request, 'account/login.html', {})
'''
