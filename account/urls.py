from django.urls import path
from . import views
app_name='account'
urlpatterns = [
    path('login', views.user_login.as_view()),
]
