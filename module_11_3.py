from pprint import pprint


def introspection_info(obj):
    return {
        'type': type(obj).__name__,
        'attributes': dir(obj),
        'methods': [attr for attr in dir(obj) if callable(getattr(obj, attr)) and not attr.startswith('__')],
        'module': getattr(obj, '__module__', 'No module'),
        'size': obj.__sizeof__() if hasattr(obj, '__sizeof__') else 'Метод __sizeof__ отсутствует',
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
