# coding: utf-8
from django.conf.urls import url
from django.http import HttpResponse


def active_view(request):
    return HttpResponse('<h1>Test view has responsed<h1>')


urlpatterns = [
    url(r'^/$', active_view),
]
