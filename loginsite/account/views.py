from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from account.models import Account
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'account/login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']

        if username is None:
            messages.error(request, "Username is required.")
        elif password is None:
            messages.error(request, "Password is required.")
        else:
            user = authenticate(request, username=username, password=password)
            #user = Account.objects.get(username=username)

            if user is not None:

                if user.email:
                    # Email exists
                    login(request, user)
                    messages.success(request, "Login successful")
                    # https://pypi.org/project/django-two-factor-auth/
                    # redirect to home page:
                    return HttpResponseRedirect(reverse('home:dashboard'))
                else:
                    # redirect to page for saving email:
                    return render(request, 'account/save_email.html', {'account_id': user.id})

            else:
                messages.error(request, "Invalid username or password")
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('account:login'))


def register(request):
    if request.method == 'GET':
        return render(request, 'account/register.html')

    else:
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']

        # account = Account.objects.get(email=email)

        if username is None:
            messages.error(request, "Username is required.")
        # elif email and account:
        #     messages.error(request, "Email address is already taken")
        elif password is None:
            messages.error(request, "Password is required.")
        elif password_confirmation is None:
            messages.error(request, "Confirmation password is required.")
        elif password != password_confirmation:
            messages.error(request, "Passwords do not match.")
        else:
            new_account = Account(username=username, first_name=first_name, last_name=last_name,
                                  email=email, password=password)
            new_account.save()

            messages.success(request, 'Account registration successful')
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('account:register'))


def save_email(request):
    if request.method == 'GET':
        return render(request, 'account/save_email.html')

    else:
        email = request.POST['email']
        id = request.POST['account_id']
        try:

            account = Account.objects.get(email=email)

            if email is None:
                messages.error(request, "Email address is required.")
            elif account:
                messages.error(request, "Email address already exists")
        except Account.DoesNotExist:  # Email address does not exist, send email
            if id:
                account = Account.objects.get(id=id)
                account.send_verification_email("Email verification")
                messages.info(request, 'A confirmation email has been sent to %s' % email)
            else:
                messages.error(request, 'Account does not exist')


    return HttpResponseRedirect(reverse('account:save_email'))


def email_confirmation(request):
    messages.info(request, "Email address has been verified")
    return render(request, 'account/login.html')
