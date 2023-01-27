from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Login_Form
# Create your views here.

class user_login(View):
    def get(self, request):
        form = Login_Form() #instans is form
        return render(request, 'account/login.html', {'form':form})

    def post(self,request):
        form = Login_Form(data=request.POST) #instans form login_form

        if form.is_valid():
            cd = form.cleaned_data #hint:is instans in next by is_vaiid

            user = authenticate(username=cd['phone'], password=cd['password']) #username=usernamecustom

            if user is not None:
                login(request, user)
                return redirect('web:home')
            else:
                form.add_error('phone','invalid data')

        else:
            form.add_error('phone', 'invalid data')
        return render(request, 'account/login.html',{'form':form})

'''
#test ok
def login(request):
    return render(request, 'account/login.html', {})
'''
