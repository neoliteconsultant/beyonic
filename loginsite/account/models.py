from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    username = models.CharField(max_length=40, unique=True, verbose_name="Username")
    first_name = models.CharField(max_length=40, verbose_name="First name")
    last_name = models.CharField(max_length=40, verbose_name="Last name")
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=60,
        unique=True,
    )
    is_first_time_login = models.BooleanField(default=True)
    created_on = models.DateTimeField('created on', auto_now=True)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username