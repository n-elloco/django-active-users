MONITORING DJANGO ACTIVE USERS
==============================

.. image:: https://img.shields.io/pypi/v/django-active-users.svg
    :target: https://pypi.python.org/pypi/django-active-users

.. image:: https://travis-ci.org/n-elloco/django-active-users.svg?branch=master
    :target: https://travis-ci.org/n-elloco/django-active-users


*Online monitoring of active users in Django using Redis*

Collecting information about active users in the Django application
for the last specified time interval using Redis cache.


Requirements
------------

- Python: 2.7, 3.3, 3.4, 3.5
- Django: 1.5+
- Django-redis: 4.4.4


Install
-------

.. code-block:: bash

    pip install django-active-users


Setup
-----

Your django application should already be setting of Redis cache. 
See more in ``django-redis`` `official documentation <http://niwinz.github.io/django-redis/latest/#_configure_as_cache_backend>`_. 

Add ``active_users.middleware.ActiveUsersSessionMiddleware`` to your project's ``MIDDLEWARE_CLASSES`` after the ``SessionMiddleware``.

.. code-block:: python

    MIDDLEWARE_CLASSES = (
        ...
        'django.contrib.sessions.middleware.SessionMiddleware',
        'active_users.middleware.ActiveUsersSessionMiddleware',
        ...
    )


Settings
--------

``ACTIVE_USERS_KEY_EXPIRE`` - Time of key expire (interval after the last request during which the visitor is considered active) in seconds. Default is 20.

``ACTIVE_USERS_EXCLUDE_URL_PATTERNS`` - List of regular expressions for excluding URLs. If they are matched, the visitor (and pageview) key will not be create.

``ACTIVE_USERS_KEY_CLASS`` - Class of visitor key entry. It should be inherited from ``active_users.keys.AbstractActiveUserEntry``. Default ``active_users.keys.ActiveUserEntry``


API
---

You can use API for getting information about active users.
You can call methods from ``active_users.api`` module directly.

**Methods:**

- ``get_active_users_count`` - returns count of active users (users, who visited site for the last time interval,
  which is set by option ``ACTIVE_USERS_KEY_EXPIRE``)

- ``get_active_users`` - returns list of dictionaries with information about active users;
  keys of dictionaries are set from field ``fields`` of entry class, which is set by option ``ACTIVE_USERS_KEY_CLASS``


Also, you can include special view in your Django application, adding the URL pattern to your ``urls.py`` file


..code-block:: python

    urlpatterns = [
        ...
        url(r'^active-users/', include('active_users.api.urls')),
        ...
    ]
