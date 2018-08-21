from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'home'

urlpatterns = [
    url('', views.dashboard, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
]
