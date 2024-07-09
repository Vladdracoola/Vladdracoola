grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

student_new = sorted(students)
grades_new = []
for lol in grades:
    newlist=sum(lol)/len(lol)
    grades_new.append(newlist)



dict=dict(zip(student_new, grades_new))
print(dict)