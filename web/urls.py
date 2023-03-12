from django.urls import path
from . import views
app_name = 'web'
urlpatterns = [
    path('', views.Home_view.as_view(), name='home')

]

