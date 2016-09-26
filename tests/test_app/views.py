# coding: utf-8
from django.conf.urls import url, include
from django.http import HttpResponse


def active_view(request):
    return HttpResponse('<h1>Test view has responded<h1>')


def excluded_view(request):
    return HttpResponse('<h1>Excluded view has responded<h1>')


_patterns = [
    url(r'^active-users/', include('active_users.api.urls')),
    url(r'^excluded/$', excluded_view),
    url(r'^$', active_view),
]

try:
    from django.conf.urls import patterns
    urlpatterns = patterns('', *_patterns)
except ImportError:
    urlpatterns = _patterns
