# coding: utf-8
import os
import sys

from django.conf import settings, global_settings


def main():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    app_name = os.path.basename(current_dir)
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
        MIDDLEWARE_CLASSES=global_settings.MIDDLEWARE_CLASSES + ('active_users.middleware.ActiveUsersSessionMiddleware',),
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.sites',
        ),
        ROOT_URLCONF=app_name + '.test_view',
    )

    settings.configure(**conf_kwargs)

    from django.test.utils import get_runner
    runner = get_runner(settings)()
    failures = runner.run_tests((app_name,))

    sys.exit(failures)


if __name__ == '__main__':
    main()
