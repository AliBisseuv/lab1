# Инициализация
print('Лабораторная работа 2. Задание №2\nМинимальный делитель в диапазоне от 2 до 30 000.')

# Бесконечный цикл
while True:

    print('\nДля завершения программы введите любой не числовой символ или число меньше 2, больше 30 000.\n')
    x = input('Введите число "x": ') 

    # Выход из бесконечного цикл
    if not x.isdigit():
        break 
    else:
        x = int(x)

    # Нахождение мимнимального делителя при вводе чисел в диапазоне от 2 до 30 000
    if not 2 < x <= 30000: break
    for i in range(2,x + 1):
        if (x % i) == 0:
            # Вывод мимнимального делителя на экран
            print(i)
            break
        else:
            continue

# Завершение работы программы
print('\n\aПока, пока ...')
