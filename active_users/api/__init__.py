# coding:utf-8
try:
    from django.utils.encoding import force_str
except ImportError:
    # FIXME: Django 2 compatibility
    from django.utils.encoding import force_text as force_str

from django_redis import get_redis_connection

from active_users.settings import active_users_settings as settings


def get_active_users_keys(pattern='au:*'):
    """ Get all keys from redis """
    return [force_str(key) for key in get_redis_connection().keys(pattern)]


def get_active_users_count():
    """ Get redis keys count """
    return len(get_active_users_keys())


def get_active_users():
    """ Get list of all active users """
    return [
        settings.KEY_CLASS.key_to_dict(key) for key in get_active_users_keys()
    ]
