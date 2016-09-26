# coding: utf-8
import json
import time

from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.test.utils import override_settings
from django_redis import get_redis_connection

from active_users.api import get_active_users_count, get_active_users
from active_users.settings import active_users_settings


class ActiveUsersTest(TestCase):

    username = 'test'
    user_password = 'secret'

    @classmethod
    def setUpClass(cls):
        super(ActiveUsersTest, cls).setUpClass()
        cls.redis_client = get_redis_connection()

        cls.key_class = active_users_settings.KEY_CLASS

        cls.client = Client()
        cls.user = User.objects.create_user(
            username=cls.username, email='test@test.com', password=cls.user_password)

    def setUp(self):
        self.client.login(username=self.username, password=self.user_password)

    def tearDown(self):
        self.redis_client.flushdb()

    def test_view(self):
        self.url_request('/')
        self.assertEqual(get_active_users_count(), 1)

        users = get_active_users()
        user = users.pop()

        self.assertEqual(user['user_id'], str(self.user.id))
        self.assertEqual(user['username'], self.username)

    @override_settings(ACTIVE_USERS_KEY_EXPIRE=3)
    def test_expire_setting(self):
        self.url_request('/')
        time.sleep(3)
        self.assertEqual(get_active_users_count(), 0)

    @override_settings(ACTIVE_USERS_EXCLUDE_URL_PATTERNS=['/excluded'])
    def test_excluded_view(self):
        self.url_request('/excluded/')
        self.assertEqual(get_active_users_count(), 0)

    def test_api_view(self):
        self.url_request('/')
        response = self.url_request('/active-users/active-users-info/')

        data = json.loads(response.content.decode())
        self.assertIn('data', data)
        self.assertIn('count', data)

    def url_request(self, url):
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        return response
