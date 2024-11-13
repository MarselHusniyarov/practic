immutable_var = 1,'string',11.59
print(immutable_var)
#immutable_var [0] = 2 # Нельзя изменить эллемент кортежа, потому что кортеж не поддерживает обращение по элементам
mutable_list = [1,'print',True]
mutable_list[0]= 13
print(mutable_list)