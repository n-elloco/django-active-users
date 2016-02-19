# coding:utf-8
from django_redis import get_redis_connection

from .settings import KEY_CLASS


def get_active_users_keys(pattern='au:*'):
    return get_redis_connection().keys(pattern)


def get_active_users_count():
    return len(get_active_users_keys())


def get_active_users():
    keys = get_active_users_keys()
    return map(KEY_CLASS.key_to_dict, keys)


