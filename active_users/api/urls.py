# coding: utf-8
from django.urls import re_path

from . import views


_patterns = [
    re_path(r'^active-users-info/$', views.active_users_info_view)
]

try:
    from django.conf.urls import patterns

    urlpatterns = patterns('', *_patterns)
except ImportError:
    urlpatterns = _patterns
