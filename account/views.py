from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect,reverse
from django.utils.crypto import get_random_string
from django.views.generic import View, UpdateView
from .forms import Login_Form,Registerform,CheckotpForm
import random
import ghasedakpack
from .models import otp,User

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
            random_code=random.randint(1000,9999)
            token=get_random_string(length=10)
            print(random_code)
            sms.verification({'receptor': cd['phone'],'type': '1','template': 'turn_rading_11','param1': str(random_code)})
            otp.objects.create(phone=cd['phone'],code=random_code,token=token)
            return redirect(reverse('account:checkotp')+f'?={token}') 
        return render(request,'account/register.html',{'form':form})       
    
    
class checkotp(View):
    def get(self,request):
        form=CheckotpForm() #instans is a ckeckotpformform null
        return render(request,'account/checkotp.html',{'form':form})

    
    def post(self,request):
        token=request.GET.get('token')#get data in url
        form=CheckotpForm(data=request.POST) #instatnse is checkotpform in data+requuest.POST
        if form.is_valid():
            cd=form.cleaned_data
            if otp.objects.filter(code=cd['code'],token=token).exists():
                Otp=otp.objects.get(token=token)
                user=User.objects.create_user(phone=Otp.phone)
                login(request,user)
            return redirect(reverse('web:home'))
        return render(request,'account/checkotp.html',{'form':form})                
    


