from django.contrib import admin

from .models import Account

# class CustomUserAdmin(UserAdmin):
# add_form = CustomUserCreationForm
# form = CustomUserChangeForm
# model = Account
# list_display = ['email', 'username']


# admin.site.register(Account, CustomUserAdmin)
admin.site.register(Account)
