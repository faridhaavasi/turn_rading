from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,reverse

from django.views.generic import View
from .forms import Login_Form,Registerform

import ghasedakpack
from .models import User

# Create your views here.



sms = ghasedakpack.Ghasedak("1fca2d5c8598fb09f04ab70c1e6c8e")
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
                return redirect('web:index')
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
class User_register(View):
    def get(self,request):
        form=Registerform() #instans is a form Registerform null
        return render(request,'account/register.html',{'form':form})
    def post(self,request):
        form = Registerform(data=request.POST)  # instatnse is checkotpform in data+requuest.POST
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create(phone=cd['phone'], fullname=cd['fullname'], file_number=cd['file_number'], password=cd['password'])
            login(request, user)
            return redirect('web:index')
        return render(request, 'account/register.html', {'form': form})





