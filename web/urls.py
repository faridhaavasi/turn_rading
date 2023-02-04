from django.urls import path
from . import views
app_name = 'web'
urlpatterns = [
    path('', views.home,  name='home'),
    path('edit/<int:pk>', views.Update_info.as_view(), name='edit'),
    path('index', views.index.as_view(), name='index'),
]