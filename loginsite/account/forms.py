from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account


# https://wsvincent.com/django-user-authentication-tutorial-login-and-logout/

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Account
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('username', 'email')
