# coding:utf-8
from django.conf import settings
from django.utils.module_loading import import_by_path

from .keys import AbstractActiveUserEntry


# Time of key expire in seconds
KEY_EXPIRE = getattr(settings, 'ACTIVE_USERS_KEY_EXPIRE', 20)
_KEY_CLASS_NAME = getattr(
    settings, 'ACTIVE_USERS_KEY_CLASS', 'active_users.keys.ActiveUserEntry')

KEY_CLASS = import_by_path(_KEY_CLASS_NAME)
EXCLUDE_URL_PATTERNS = getattr(
    settings, 'ACTIVE_USERS_EXCLUDE_URL_PATTERNS', [])

assert issubclass(KEY_CLASS, AbstractActiveUserEntry)
