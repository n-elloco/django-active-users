# coding:utf-8
import re

from django.utils.functional import cached_property
from django_redis import get_redis_connection

from .settings import KEY_EXPIRE, KEY_CLASS, EXCLUDE_URL_PATTERNS


class ActiveUsersSessionMiddleware(object):

    @cached_property
    def redis_client(self):
        return get_redis_connection()

    def process_request(self, request):
        if EXCLUDE_URL_PATTERNS:
            if any(re.search(pat, request.path) for pat in EXCLUDE_URL_PATTERNS):
                return
        if request.user.id is not None:
            key = KEY_CLASS.create_from_request(request)
            self.redis_client.setex(
                name=key.dump(),
                value=0,
                time=KEY_EXPIRE
            )
