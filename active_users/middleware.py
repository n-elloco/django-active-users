# coding:utf-8
import re

from django.utils.functional import cached_property
from django_redis import get_redis_connection

from active_users.settings import active_users_settings as settings

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    parent_class = object
else:
    parent_class = MiddlewareMixin


class ActiveUsersSessionMiddleware(parent_class):

    @cached_property
    def redis_client(self):
        return get_redis_connection()

    def process_request(self, request):
        if settings.EXCLUDE_URL_PATTERNS:
            if any(re.search(pat, request.path)
                   for pat in settings.EXCLUDE_URL_PATTERNS):
                return
        if request.user.id is not None:
            key = settings.KEY_CLASS.create_from_request(request)
            self.redis_client.setex(
                name=key.dump(),
                value=0,
                time=settings.KEY_EXPIRE
            )
