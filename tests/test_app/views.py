# coding: utf-8
from django.conf.urls import include
from django.http import HttpResponse
from django.urls import re_path


def active_view(request):
    return HttpResponse('<h1>Test view has responded<h1>')


def excluded_view(request):
    return HttpResponse('<h1>Excluded view has responded<h1>')


_patterns = [
    re_path(r'^active-users/', include('active_users.api.urls')),
    re_path(r'^excluded/$', excluded_view),
    re_path(r'^$', active_view),
]

try:
    from django.conf.urls import patterns
    urlpatterns = patterns('', *_patterns)
except ImportError:
    urlpatterns = _patterns
