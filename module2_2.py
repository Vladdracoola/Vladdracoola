first=int(input('Введите число: '))
second=int(input('Введите число: '))
third=int(input('Введите число: '))
set={first,second,third}
if len(set)==1:
    print(3)
elif len(set)==2:
    print(2)
else:
    print(0)