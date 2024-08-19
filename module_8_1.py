def add_everything_up(a,b):
    try:
        result = a + b
    except TypeError:
        a = str(a)
        b = str(b)
        result = a + b
        return f'Странное желание - странный результат! {result}'

    else:
        return f'Слушаюсь и повинуюсь! {result}'



print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))







