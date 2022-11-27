# Инициализация
print('Лабораторная работа 2. Задание №7\nПрограмма вывода результата голосования')

def voting_results(flag: int, my_list: list) -> None:
    ''' Вывод результата голосования '''
    if f == 0 and sum(my_list) >= 2:
        print('Результат: True')
    if f == 0 and sum(my_list) < 2:
        print('Результат: False')
        
# Бесконечный цикл
while True:

    # Пригласительная строка
    print('\nДля завершения программы:'
          '1 способ: введите любой не числовой символ,'
          '2 способ: число не равное "0" или "1"'
          '2 способ: ввод подряд 2 и более символов "0" или "1"\n')

    # Фиксация "голосов" 
    input_numbers = input('Введите  голоса (1 или 0), разделив пробелом (пробелами) или клавишей "Tab": ')
    my_list = input_numbers.split()
    for i in my_list:
        i.replace(' ', '')
        i.replace('chr(9)', '')
    if len(my_list) < 3: break
    a = my_list[0]
    b = my_list[1]
    c = my_list[2]

    # Определение корректности ввода
    if  not a.isdigit() or not b.isdigit() or not c.isdigit():
        f = 1
        print('Не корректно введены числа. Програма завершена.')
        break
    my_list = [int(a), int(b), int(c)]
    for i in my_list:
        if (i < 0) or (i > 1):
            print('Не корректно введены числа. Програма завершена.')
            f = 1
            break
        else:
            f = 0

    # Выход из бесконечного цикла
    if f == 1: break

    voting_results(f, my_list)

# Завершение работы программы
print('\n\aПока, пока ...')
