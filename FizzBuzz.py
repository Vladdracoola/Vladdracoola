a='Fizz'
b='Buzz'
c='FizzBuzz'
score={}
i = 0
name=input('Введите имя: ')
for i in range(99):
    number=int(input('Чтобы выиграть, надо получить число FizzBuzz,  '))
    score.update({name:i+1})
    if number%3==0 and number%5==0:

        print(c ,'Ты настоящий гений,', name)
        print('Затрачено попыток:', score)
        break

    elif number%3==0:
        print(a ,'Осталось попыток:', 98-i)
        continue
    elif number%5==0:
        print(b ,'Осталось попыток:', 98-i)
        continue

    else:
         print('Нифизнибасникарабас')
         answer=(input("Для выхода введите 'n'" ))
    if answer == 'n':
        print('GG')
        break


    if answer == '':
        print('Осталось попыток:', 98-i)
        continue
