from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'account'

urlpatterns = [
    url(r'^$', views.index),
    path('', views.index, name="login"),
    path('register', views.register, name="register"),
]
