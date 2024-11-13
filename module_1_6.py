my_dict = {'name' : 'Marsel', 'Bd' : 2002}
print(my_dict)
print("Существующее значение : ", my_dict.get('name'))
print("Несуществующее значение : ", my_dict.get('age'))
my_dict.update({'Age' : 22, 'Country' : 'Russian Federation', 'Town' : 'Kazan'})
deleted = my_dict.pop('Country')
print(deleted)
print(my_dict)


my_set = {1,1,'apple','apple',12.44,12.44}
print(my_set)
my_set.add(9)
my_set.add((15,12,11,14))
my_set.discard(1)
print(my_set)
