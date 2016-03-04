MONITORING DJANGO ACTIVE USERS
==============================

Monitoring of active users in Django using Redis


Requirements
------------

- Python: 2.7
- Django: 1.6, 1.7
- Django-redis: 4.30


Install
-------

```bash
pip install django-active-users
```


Setup
-----

Your django application should already be setting of Redis cache. 
See more in [official documentation](http://niwinz.github.io/django-redis/latest/#_configure_as_cache_backend) of `django-redis`

Add `active_users.middleware.ActiveUsersSessionMiddleware` to your project's `MIDDLEWARE_CLASSES` after the `SessionMiddleware`.

```python
MIDDLEWARE_CLASSES = (
    ...
    'django.contrib.sessions.middleware.SessionMiddleware',
    'active_users.middleware.ActiveUsersSessionMiddleware',
    ...
)
```

Settings
--------

`ACTIVE_USERS_KEY_EXPIRE` - Time of key expire (interval after the last request during which the visitor is considered active) in seconds. Default is 20.

`ACTIVE_USERS_EXCLUDE_URL_PATTERNS` - A list of regular expressions that will be matched
against the `request.path_info`. If they are matched, the visitor (and pageview) key will not
be create.

`ACTIVE_USERS_KEY_CLASS` - Class of visitor key entry. It should inherited from `active_users.keys.AbstractActiveUserEntry`. Default `active_users.keys.ActiveUserEntry`


