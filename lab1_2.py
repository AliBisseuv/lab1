# Задание № 2 

# Инициализация
print('Нахождение числа десятков в заданном числе')

# Бесконечный цикл
while True:

    # Пригласительная строка
    print('\nДля завершения программы введите отрицательное число.\n')

    # Ввод числа
    a = input('Введите число: ')

   # Выход из бесконечного цикла
    if not a.isdigit(): break   

    # Находжение числа десятков
    a = (int(a) % 100) // 10
    print(f'Число десятков равно: {a}')

# Завершение работы программы
print('\n\aПока, пока ...')