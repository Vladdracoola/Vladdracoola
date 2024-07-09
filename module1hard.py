journal={}
i = 0
for i in range(99):
 student_name=input('Введите имя ученика: ',)
 student1=list(input('Введите оценки слитно:'))
 quantity=int(len(student1))
 print('Ученик' ,student_name)
 marks=(student1)
 marks=[int(item) for item in marks]
 print('Оценки:', marks)
 average=(sum(marks)/quantity)
 average=round(average,2)
 journal.update({student_name: average})
 print('Средний балл: ',average)
 if input('Продолжить?[y/n] ') == 'n':
     break
 else:
     continue
print(journal)



