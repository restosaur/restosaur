from .utils import Collection
from . import serializers


class RepresentationAlreadyRegistered(Exception):
    pass


class UnknownRepresentation(Exception):
    pass


class ValidatorAlreadyRegistered(Exception):
    pass


def _pass_through_trasnform(x, ctx):
    return x


def _pass_through_validation(x, ctx):
    return x


class Representation(object):
    def __init__(
            self, vnd=None, content_type='application/json', serializer=None,
            _transform_func=None):

        self.serializer = serializer or serializers.get(content_type)
        self.content_type = content_type
        self.vnd = vnd
        self._transform_func = _transform_func or _pass_through_trasnform

    def render(self, context, obj):
        """
        Renders representation of `obj` as raw content
        """
        if isinstance(obj, Collection):
            items = map(
                lambda x: self._transform_func(x, context), obj.iterable)
            data = {
                    obj.key: items,
                    obj.totalcount_key: len(obj.iterable),
                    }
        else:
            data = self._transform_func(obj, context)
        return self.serializer.dumps(data)


class Validator(object):
    def __init__(
            self, vnd=None, content_type='application/json',
            serializer=None, _validator_func=None):

        self.serializer = serializer or serializers.get(content_type)
        self.content_type = content_type
        self.vnd = vnd
        self._validator_func = _validator_func or _pass_through_validation

    def parse(self, context):
        """
        Parses raw representation content and builds object
        """
        return self._validator_func(self.serializer.loads(context), context)
