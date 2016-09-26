# coding: utf-8
import json
from django.http import HttpResponse

from . import get_active_users


def active_users_info_view(request):
    """ View for info about active users """
    data = get_active_users()
    # Compatible with Django 1.5, 1.6
    return HttpResponse(
        json.dumps({'data': data, 'count': len(data)}, ensure_ascii=False),
        content_type='application/json')
