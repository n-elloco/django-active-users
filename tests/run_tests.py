# coding: utf-8
import os
import sys

from django.conf import settings


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, os.path.join(current_dir, '..'))

    conf_kwargs = dict(
        CACHES={
            'default': {
                'BACKEND': 'django_redis.cache.RedisCache',
                'LOCATION': 'redis://127.0.0.1:6379/0',
            }
        },
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': 'test.db',
                'TEST_NAME': 'test.db'
            }
        },
        SITE_ID=1,
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'active_users.middleware.ActiveUsersSessionMiddleware',
        ),
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
        ),
        ROOT_URLCONF='test_app.views',
    )

    settings.configure(**conf_kwargs)

    try:
        # For django>=1.7
        from django import setup
    except ImportError:
        pass
    else:
        setup()

    from django.test.utils import get_runner
    runner = get_runner(settings)()
    return runner.run_tests(('test_app',))


if __name__ == '__main__':
    failures = main()
    sys.exit(failures)
