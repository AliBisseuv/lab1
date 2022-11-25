# Лабораторная работа 2. Задание №6

# Инициализация
print('Возведение в степень "n" по основанию "a"')

def  defining_negative_number (s: str) -> int:
    # Определение отрицательного числа (negative number) и установка флага f=1, если число отрицательное
    if (s.startswith('-')) and (s.count('-') == 1) and (s.replace('-', '').isdigit()):
        f = 1
    elif s.count('.') == 1:
        f = 1
    elif s.count(',') == 1:
        f = 1
    else:
        f = 0
    return  f

def exponentiation_of_number (float_number: float, int_number: int) -> float:
    a = 1
    for i in range(int_number):
        a = a * float_number
    return a
        
# Бесконечный цикл
while True:

    # Пригласительная строка
    print('\nДля завершения программы введите любой не числовой символ, отрицательное или вещественное число "n".\n')

    a = input('Введите число "а": ') 
    flag = defining_negative_number(a)
    if a.count('.') == 1:
        f = 1
    elif a.count(',') == 1:
        f = 1
        a = a.replace(',', '.')
        
    # Выход из бесконечного цикл
    if not a.isdigit() and flag == 0 : break 

    # Ввод числа "n"
    n = input('Введите число "n": ')

    # Выход из бесконечного цикл
    if not n.isdigit(): break 

    # Перевод чисел a и b из строковой в числовой тип
    a, n = float(a), int(n)

    # Возведение числа "a" в степень "n"
    print(f'Возведение числа "{a}" в степень "{n}" равно: {exponentiation_of_number(a, n)}')

# Завершение работы программы
print('\n\aПока, пока ...')