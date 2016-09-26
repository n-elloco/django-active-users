# coding: utf-8
from django.conf.urls import url

from . import views


_patterns = [
    url(r'^active-users-info/$', views.active_users_info_view)
]

try:
    from django.conf.urls import patterns
    urlpatterns = patterns('', *_patterns)
except ImportError:
    urlpatterns = _patterns
