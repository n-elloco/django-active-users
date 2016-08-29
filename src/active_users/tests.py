# coding: utf-8
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import RequestFactory, TestCase


def active_view(request):
    return HttpResponse('<h1>Test view has responsed<h1>')


class ActiveUsersTest(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test', email='test@test.com', password='secret')

    def test_view(self):
        request = self.factory.get(active_view)
        request.user = self.user
        response = active_view(request)

        self.assertEqual(response.status_code, 200)

