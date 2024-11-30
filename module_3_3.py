def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print('--------------------------------')

print_params(2, 'столбец', False)
print_params(3, 'None')
print_params(a='один', b='два', c='три')
print_params(a='один', b='два')
print_params(a='один')
print_params()
print('--------------------------------')

print_params(b=25)
print_params(c=[1, 2, 3])
print('--------------------------------')

values_list = [9.8, 'const', True]
values_dict = {'a': 'else', 'b': False, 'c': 0}
print_params(*values_list)
print_params(**values_dict)
print('--------------------------------')

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)