from django.test import TestCase


class HomeTestCase(TestCase):

    def test_dashboard(self):
        response = self.client.get('/home/dashboard/')
        self.assertEqual(response.status_code, 200)
