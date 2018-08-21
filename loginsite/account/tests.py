from django.test import TestCase
from account.models import Account
from django.urls import reverse
from unittest import skip
from django.contrib.messages import get_messages, SUCCESS, ERROR


class AccountTestCase(TestCase):
    def setUp(self):
        Account.objects.create(username="misterb", email="misterb@gmail.com", password="b#891")

    def test_string_representation(self):
        account = Account(username="tony")
        self.assertEqual(str(account), account.username)

    # @skip("Don't want to test")
    def test_login(self):
        response = self.client.get('/account/login')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/account/register')
        self.assertEqual(response.status_code, 200)

    def test_successful_login(self):
        Account.objects.create(username="beyonic", first_name="",
                               last_name="", email="", password="b#891")
        response = self.client.post(reverse('account:login'), {'username': "beyonic", 'password': "b#891"})
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Login successful')
        self.assertRedirects(response, reverse('home:dashboard'), status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_login_invalid_credentials(self):
        response = self.client.post(reverse('account:login'), {'username': "beyonic", 'password': "2484284"})
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), "Invalid username or password")
        self.assertEqual(messages[0].level, ERROR)
        self.assertRedirects(response, reverse('account:login'), status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_successful_registration(self):
        response = self.client.post(reverse('account:register'), {'username': "markj", 'first_name': 'Mark',
                                                                  'last_name': 'Johnson', 'email': 'markj@gmail.com',
                                                                  'password': '24r4^j',
                                                                  'password_confirmation': '24r4^j'})
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Account registration successful')
        self.assertEqual(messages[0].level, SUCCESS)
        self.assertRedirects(response, reverse('account:register'), status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)

    def test_successful_registration_missing_fields(self):
        """Test for registration when email, first name and last name are not provided"""
        response = self.client.post(reverse('account:register'), {'username': "honcho",
                                                                  'first_name': '',
                                                                  'last_name': '', 'email': '',
                                                                  'password': '24r4383',
                                                                  'password_confirmation': '24r4383'})
        self.assertEqual(response.status_code, 302)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Account registration successful')
        self.assertEqual(messages[0].level, SUCCESS)
        self.assertRedirects(response, reverse('account:register'), status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)

