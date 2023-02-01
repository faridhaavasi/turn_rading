from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import Login_Form,Registerform
import random
import ghasedakpack
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
class User_register(View):
    def get(self,request):
        form=Registerform() #instans is a form Registerform null
        return render(request,'account/register.html',{'form':form})


    def post(self,request):
        form=Registerform(data=request.POST) #instatnse is registerfom in data+requuest.POST
        if form.is_valid():
            cd=form.cleaned_data
            code=random.randint(1000,9999)
            sms.verification({'receptor': cd['phone'],'type': '1','template': '	turn_rading_11','param1': str(code)})
        return render(request,'account/register.html',{'form':form})       
         
        