import threading
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template


class AccountManager(BaseUserManager):
    def create_user(self, username, password=None):
        """Creates and saves a User with the given username and password."""
        user = self.model(
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,  username, email, password):
        """Creates and saves a super user with the given username and password."""
        user = self.model(
            username=username,
            email=email,
            password=password,
        )

        user.is_admin = True
        user.save(using=self._db)


class Account(AbstractUser):
    """Model representing a user."""
    username = models.CharField(max_length=40, unique=True, verbose_name="Username")
    first_name = models.CharField(max_length=40, verbose_name="First name", null=True, blank=True)
    last_name = models.CharField(max_length=40, verbose_name="Last name", null=True, blank=True)
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=60, null=True, blank=True
    )
    is_first_time_login = models.BooleanField(default=True)
    created_on = models.DateTimeField('created on', auto_now_add=True)

    objects = AccountManager()

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'

    def __str__(self):
        """String for representing the Model object."""
        return self.username

    def send_verification_email(self, subject):
        """Send an email for verifying email address added by user"""
        # email_thread = EmailThread(self.id, self.username, subject, self.email)
        email_thread = EmailThread(self.id, "Tonym", subject, "neoliteconsultant@gmail.com")
        email_thread.start()


class EmailThread(threading.Thread):
    def __init__(self, account_id, username, subject, recipient_email):
        threading.Thread.__init__(self)
        self.account_id = account_id
        self.username = username
        self.subject = subject
        self.recipient_email = recipient_email

    def run(self):
        html_template = get_template('account/email/email_confirmation.html')
        plaintext_template = get_template('account/email/email_confirmation.txt')

        params = {'username': self.username, 'accountId': self.account_id}

        text_content = plaintext_template.render(params)
        html_content = html_template.render(params)

        msg = EmailMultiAlternatives(self.subject, text_content, settings.EMAIL_HOST_USER, [self.recipient_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send(fail_silently=False)
