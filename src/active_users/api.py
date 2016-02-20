# coding:utf-8
from django_redis import get_redis_connection

from .settings import KEY_CLASS


def get_active_users_keys(pattern='au:*'):
    """ Get all keys from redis """
    return get_redis_connection().keys(pattern)


def get_active_users_count():
    """ Get redis keys count """
    return len(get_active_users_keys())


def get_active_users():
    """ Get list of all active users """
    return map(KEY_CLASS.key_to_dict, get_active_users_keys())
