from django.test import TestCase
from account.models import Account
from django.urls import reverse
from unittest import skip

class AccountTestCase(TestCase):
    # def setUp(self):
    #     Account.objects.create(username="beyonic", password="b#891")
    #     Account.objects.create(username="misterb", email="misterb@gmail.com", password="b#891")

    def test_string_representation(self):
        account = Account(username="tony")
        self.assertEqual(str(account), account.username)

    #@skip("Don't want to test")
    def test_homepage(self):
        response = self.client.get('/account/')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        response = self.client.get('/account/register')
        self.assertEqual(response.status_code, 200)

    @skip("Don't want to test")
    def test_successful_login(self):
        response = self.client.post(reverse('account:login'), {'username': "beyonic", 'password': "b#891"})
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'account/login.html')
        self.assertRedirects(response, '/home/home', status_code=302,
                             target_status_code=200, msg_prefix='', fetch_redirect_response=True)


