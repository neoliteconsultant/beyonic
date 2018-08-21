from django.urls import path
from django.conf.urls import url
from two_factor.urls import urlpatterns as tf_urls

from . import views

app_name = 'account'

urlpatterns = [
    url(r'^$', views.sign_in),
    url('login', views.sign_in, name="login"),
    url('save_email', views.save_email, name='save_email'),
    url('email_confirmation', views.email_confirmation, name='email_confirmation'),
    path('register', views.register, name="register"),
]
