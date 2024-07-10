my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
while my_list[0] >= 0:
    number = my_list.pop(0)
    if number == 0:
        continue
    print(number)
    if len(my_list) < 1:
        break
