# Задание № 6

# Инициализация
print('Сравнение трех чисел')

# Бесконечный цикл
while True:

    # Пригласительная строка
    print('\nДля завершения программы введите любой не числовой символ \n')

    f = 0
    # Ввод 1-го числа
    x1 = input('Введите первое число: ') 

    # Определение отрицательного числа и установка флага f=1, если число отрицательное
    if (x1.startswith('-')) and (x1.count('-') == 1) and (x1.replace('-', '').isdigit()):
        f = 1

    # Выход из бесконечного цикл
    if not x1.isdigit() and f == 0 : break 

    # Ввод 2-го числа
    x2 = input('Введите второе число: ')

    # Определение отрицательного числа и установка флага f=1, если число отрицательное
    if (x2.startswith('-')) and (x2.count('-') == 1) and (x2.replace('-', '').isdigit()):
        f = 1

    # Выход из бесконечного цикл
    if not x2.isdigit() and f == 0 : break 

    # Ввод 3-го числа
    x3 = input('Введите третье число: ')
    # Определение отрицательного числа и установка флага f=1, если число отрицательное
    if (x3.startswith('-')) and (x3.count('-') == 1) and (x3.replace('-', '').isdigit()):
        f = 1

    # Выход из бесконечного цикл
    if not x3.isdigit() and f == 0 : break 

    # Сравнение чисел
    # Если первое число больше второго числа
    x4 = int(x1) if int(x1) > int(x2) else int(x2)

    # Если наибольшее из первух двух введенных чисел  меньше 3 числа
    x4 = int(x3) if x4 < int(x3) else x4
    print (f'Наибольшее число из {x1}, {x2}, {x3} равно: {x4}')

# Завершение работы программы
print('\n\aПока, пока ...')