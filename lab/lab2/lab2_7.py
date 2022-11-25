# Лабораторная работа 2. Задание №7

# Инициализация
print('Программа вывода результата голосования')

def voting_results(flag: int, my_list: list) -> None:
    ''' Вывод результата голосования '''
    if f == 0 and sum(my_list) >= 2:
        print('True')
    if f == 0 and sum(my_list) < 2:
        print('False')
        
# Бесконечный цикл
while True:

    # Пригласительная строка
    print('\nДля завершения программы введите любой не числовой символ, число не равное "0" или "1".\n')

    # Фиксация "голосов" 
    my_list = []
    for i in range(1, 4):
        x = input(f'Введите {i} голос (1/0): ')

    # Определение корректности ввода
        if len(x) > 1:
            f = 1
            break 
        elif not x.isdigit():
            f = 1
            break            
        # elif int(x) < 0:
        #     print('Не корректное число. Програма завершена.')
        #     f = 1
        #     break
        elif int(x) > 1:
            print('Не корректное число. Програма завершена.')
            f = 1
            break
        else:
            f = 0
            my_list.append(int(x))
    voting_results(f, my_list)

    # Выход из бесконечного цикла
    if f == 1: break

# Завершение работы программы
print('\n\aПока, пока ...')