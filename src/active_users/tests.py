# coding: utf-8
from django.contrib.auth.models import User
from django.test import TestCase, Client

from active_users.test_view import active_view


class ActiveUsersTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test', email='test@test.com', password='secret')
        self.client.login(username='test', password='secret')

    def test_view(self):
        request = self.client.get('/')
        response = active_view(request)

        self.assertEqual(response.status_code, 200)
