# coding:utf-8
from django.conf import settings
from django.test.signals import setting_changed
try:
    from django.utils.module_loading import import_string
except ImportError:
    from django.utils.module_loading import import_by_path as import_string

from active_users.keys import AbstractActiveUserEntry


PREFIX = 'ACTIVE_USERS'

DEFAULTS = {
    'KEY_EXPIRE': 20,
    'KEY_CLASS': 'active_users.keys.ActiveUserEntry',
    'EXCLUDE_URL_PATTERNS': []
}


class ActiveUsersSettings(object):

    def __init__(self):
        for key, default in DEFAULTS.items():
            value = getattr(settings, '{0}_{1}'.format(PREFIX, key), default)
            self.set_setting(key, value)

        assert issubclass(self.KEY_CLASS, AbstractActiveUserEntry)

    def set_setting(self, key, value):
        setattr(
            self, key, import_string(value) if key == 'KEY_CLASS' else value)


active_users_settings = ActiveUsersSettings()


def reload_settings(*args, **kwargs):
    if kwargs['setting'].startswith(PREFIX):
        key = kwargs['setting'].replace(PREFIX + '_', '')
        if key in DEFAULTS:
            active_users_settings.set_setting(
                key, kwargs['value'] or DEFAULTS[key])


setting_changed.connect(reload_settings)
