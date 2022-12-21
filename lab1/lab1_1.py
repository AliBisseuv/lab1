# Задание № 1 

# Инициализация
print('Программа расчета гипотенузы по известным катетам в прямоугольном треугольнике')

# Бесконечный цикл
while True:

    # Пригласительная строка
    print('\nДля завершения программы введите отрицательное число или число более 1000, любой не числовой символ.\n')

    # Ввод числа "А"
    a = input('Введите значение катета "А": ')

    # Проверка коректности ввода числа "А" 
    if (not a.isdigit()) or (int(a) < 0) or (int(a) > 1000): break

    # Ввод числа "B"
    b = input('Введите значение катета "B": ')

    # Проверка коректности ввода числа "B"
    if (not b.isdigit()) or (int(b)<0) or (int(b)>1000): break

    # Расчет гипотенузы
    print(f'Гипотенуза прямоугольного треугольника с катетама А = {a} и В = {b} равна: {(int(a) ** 2 + int(b) ** 2) ** 0.5}')

# Завершение работы программы
print('\n\aПока, пока ...')