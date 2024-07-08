my_dict = {'Spring': ['March', 'April', 'May'], 'Year':[1,2,True]  }
print(my_dict)
print(my_dict.get('Spring'), 'No way')
my_dict.update({'John': 'Dawson','Petr': 77})
x=my_dict.pop('Year')
print(x)
print(my_dict)

my_set = {2,3,4,True,6,7,8,True}
print(my_set)
x='String'
my_set.update({5,x,1})#Почему не добавляется 1?
my_set.discard(True)
print(my_set)