from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView,UpdateView
from account.models import User
# Create your views here.
from .forms import edit_info_form

def home(request):
    return render(request, 'web/home.html')


class index(TemplateView):
    template_name = 'web/index.html'

class Update_info(UpdateView):
    model = User
       # specify the field

    #fields=('fullname','file_number','password')

    form_class = edit_info_form

    template_name='web/update_ino.html'
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url = reverse_lazy('/')
    