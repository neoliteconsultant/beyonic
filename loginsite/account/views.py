from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'account/login.html')


def login(request):
    return HttpResponse("Hello, world.")


def register(request):
    return render(request, 'account/register.html')




