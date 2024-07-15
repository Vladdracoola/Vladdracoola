calls = 0
list_to_search = []

while 1 > 0:
    print('***********')
    string = str(input('Введите текст: '))



    def count_calls():
        global calls
        print('Количество вызовов: ',calls)
        return


    def string_info():
        global calls
        calls += 1
        string_mod = print((len(string), string.upper(), string.lower()))
        return


    def is_contains():
        global calls
        calls += 1
        return string in list_to_search


    string_info()
    print(is_contains())
    count_calls()

    list_to_search.append(string)

    Repeat_check = input('Repeat? [enter/n] ')
    if Repeat_check == 'n':
        break
    else:
        continue
