data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

def function_main(*args):
    sum_list = 0
    for element in args:
        if isinstance(element, str):
            sum_list += len(element)
        elif isinstance(element, int):
            sum_list += element
        elif isinstance(element, list) or isinstance(element, tuple) or isinstance(element, set):
            sum_list += function_main(*element)
        elif isinstance(element, dict):
            sum_list += function_main(*element.values())
            sum_list += function_main(*element.keys())
    return sum_list


print(function_main(
  [[1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]))
