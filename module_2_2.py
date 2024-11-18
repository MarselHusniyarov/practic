first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and first == third and second == third: # Сравнение всех трех чисел между собой
        print('Все три числа равны')
elif first == second or first == third and first == first: # Сравнение первого числа с другими
        print('Равны только два числа')
elif second == third or second == first and second == second: # Сравнение второго числа с другими
        print('Равны только два числа')
elif third == first or third == second and third == third: # Сравнение третьего числа с другими
        print('Равны только два числа')
else:
        print('Нет равных чисел')