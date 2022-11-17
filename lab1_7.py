# Задание № 7

# Инициализация
print('Ход Ладьи')

# Бесконечный цикл
while True:

    # Пригласительная строка
    print('\nДля завершения программы введите любой не числовой символ, целое число меньше 1 или больше 8 \n')

    # Ввод 1-й координаты Ладьи
    x1 = input('Введите 1-ю координату Ладьи: ')

    # Выход из бесконечного цикл
    if not x1.isdigit() or int(x1) < 1 or int(x1) > 8: break 

    # Ввод 2-й координаты Ладьи
    x2 = input('Введите 2-ю координату Ладьи: ')

    # Выход из бесконечного цикл
    if not x2.isdigit() or int(x2) < 1 or int(x2) > 8: break 

    # Ввод 1-й координаты шахматной фигуры
    y1 = input('Введите 1-ю координату шахматной фигуры: ')

    # Выход из бесконечного цикл
    if not y1.isdigit() or int(y1) < 1 or int(y1) > 8: break 

    #  Ввод 2-й координаты шахматной фигуры
    y2 = input('Введите 2-ю координату шахматной фигуры: ')

    # Выход из бесконечного цикл
    if not y2.isdigit() or int(y2) < 1 or int(y2) > 8: break 

    # Определение корректности ввода координат шахматных фигур
    if int(x1) == int(y1) and int(x2) == int(y2):
        print ('Координаты шахматных фигур совпали и необходимо ввести заново их координаты.')
        continue

    # Определение взятие Ладьей шахматной фигуры
    if int(x1) == int(y1) or int(x1) == int(y2) or int(x2) == int(y1) or int(x2) == int(y2):
        r = 'YES'
    else:
        r = 'NO'
    print (f'\nЛадья с координатами {x1},{x2} может забрать шахматную фигуру с координатами {y1},{y2}?\nОтвет: {r} ')

# Завершение работы программы
print('\n\aПока, пока ...')