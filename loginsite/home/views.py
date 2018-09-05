from django.shortcuts import render
from django.contrib.auth import logout
from django.core.exceptions import PermissionDenied


def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        return render(request, 'home/dashboard.html', {"username": username})
    else:
        raise PermissionDenied

def logout_employer(request):
    logout(request)
    return render(request, 'account/login.html')
