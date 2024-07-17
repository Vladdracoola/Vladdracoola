def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1,'string', False]
values_dict = {'a': 15, 'b': 'String', 'c': '0.5'}

print_params(*values_list)
print_params(**values_dict)

values_list2 = ['Orgrimar',99]
print_params(*values_list2, 42)