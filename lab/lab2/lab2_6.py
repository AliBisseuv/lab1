# Лабораторная работа 2. Задание №6

# Инициализация
print('Лабораторная работа 2. Задание №6\nВозведение в степень "n" по основанию "a"')

def  defining_negative_number (s: str) -> int:
    # Определение отрицательного числа (negative number) и установка флага f=1, если число отрицательное
    if (s.startswith('-')) and (s.count('-') == 1) and (s.replace('-', '').isdigit()):
        f = 1
    elif s.count('.') == 1:
        f = 1
    else:
        f = 0
    return  f

def exponentiation_of_number (float_number: float, int_number: int) -> float:
    a = 1
    for i in range(int_number):
        a *= float_number
    return a

# Бесконечный цикл
while True:

    # Пригласительная строка
    print('\nДля завершения программы:\n'
             '1 способ: введите любой не числовой символ,\n'
             '2 способ: отрицательное или вещественное число "n",\n'
             '3 способ: менее двух чисел,\n'
             '4 способ: при нажатий "Enter" без ввода чисел.\n')

    input_numbers = input('Введите число "а" и "n", разделив пробелом (пробелами): ')
    numbers = input_numbers.split()
    for i in numbers:
        i.replace(' ', '')
        i.replace('chr(9)', '')
    if len(numbers) < 2: break
    
    if numbers[0].count(',') == 1:
        numbers[0] = numbers[0].replace(',', '.')
    flag = defining_negative_number(numbers[0])

    # Выход из бесконечного цикл
    if not numbers[0].isdigit() and flag == 0: break
    if not numbers[1].isdigit(): break

    # Перевод чисел a и b из строковой в числовой тип
    a, n = float(numbers[0]), int(numbers[1])

    # Возведение числа "a" в степень "n"
    print(f'Возведение числа "{a}" в степень "{n}" равно: {exponentiation_of_number(a, n)}')

# Завершение работы программы
print('\n\aПока, пока ...')
