from pprint import pprint
import sys


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': [attr for attr in dir(obj) if callable(getattr(obj, attr))],
        'methods': [attr for attr in dir(obj) if callable(getattr(obj, attr)) and not attr.startswith('__')],
        'module': obj.__class__.__module__,
        'size': sys.getsizeof(obj) if hasattr(obj, 'sizeof') else 'No sizeof method',
        'value': getattr(obj, 'value', 'No value attribute')
    }


class Sifera:
    def __init__(self, value):
        self.value = value

    def bienvenidos(self):
        return '¡Hola! ¿Qué tal?'


obj = Sifera(42)
number_info = introspection_info(obj)
pprint(number_info)
