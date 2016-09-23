# coding:utf-8
from six import text_type


class AbstractActiveUserEntry(object):
    """ Abstract class for redis key instance"""

    fields = tuple()
    key_prefix = 'au'

    def __init__(self):
        for field in self.fields:
            setattr(self, field, u'')

    @classmethod
    def create_from_request(cls, request):
        """ Fill object from request """
        raise NotImplementedError

    @classmethod
    def create_from_key(cls, key):
        """ Load object from redis key """
        key_items = key.split(u':')
        instance = cls()
        # First item is prefix
        for i, field in enumerate(cls.fields, start=1):
            setattr(instance, field, key_items.get(i, u''))
        return instance

    def dump(self):
        """ Dump object to redis key """
        key_items = [self.key_prefix]
        for field in self.fields:
            key_items.append(getattr(self, field, u''))
        return u':'.join(map(text_type, key_items))

    @classmethod
    def key_to_dict(cls, key):
        """ Convert redis key to dict directly """
        key_items = key.split(u':')[1:]  # First item is prefix
        return dict(zip(cls.fields, key_items))

    def to_dict(self):
        """ Serialize object to dict """
        return {field: getattr(self, field) for field in self.fields}


class ActiveUserEntry(AbstractActiveUserEntry):
    """ Default key class"""
    fields = ('user_id', 'session_id', 'ip', 'username')

    @classmethod
    def create_from_request(cls, request):
        instance = cls()
        if request.user.id is not None:
            instance.user_id = request.user.id
            instance.username = request.user.username
            instance.ip = cls.get_client_ip(request)
        if request.session:
            instance.session_id = request.session.session_key
        return instance

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR', '127.0.0.1')
        return ip
