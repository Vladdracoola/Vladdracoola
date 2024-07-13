import random
number = random.randint(3, 20)
list_ = []
for i in range(1, number + 1):
    for j in range(1, number + 1):
        summary_1 = i + j
        if number % summary_1 == 0 and j > i:
            list_.append(i)
            list_.append(j)
print('Число', number,'Шифр:', *list_)


