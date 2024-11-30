def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Если длина строки больше 1, отделяем первую цифру и продолжаем рекурсию
    if len(str_number) > 1:
        first = int(str_number[0])  # Первая цифра
        # Если первая цифра не 0, продолжаем умножение
        if first != 0:
            return first * get_multiplied_digits(int(str_number[1:]))
        else:
            # Если первая цифра 0, пропускаем её и рекурсивно продолжаем с оставшейся частью
            return get_multiplied_digits(int(str_number[1:]))
    else:
        # Если в числе осталась только одна цифра, возвращаем её
        return int(str_number) if str_number != "0" else 1  # Если осталась цифра 0, возвращаем 1 (по логике умножения)


result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030)
print(result2)