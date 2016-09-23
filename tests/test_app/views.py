# coding: utf-8
from django.conf.urls import url
from django.http import HttpResponse


def active_view(request):
    return HttpResponse('<h1>Test view has responded<h1>')


def excluded_view(request):
    return HttpResponse('<h1>Excluded view has responded<h1>')

urlpatterns = [
    url(r'^/$', active_view),
    url(r'^/excluded$', active_view),
]
