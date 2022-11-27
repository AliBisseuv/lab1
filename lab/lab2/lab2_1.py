# Инициализация
print('Лабораторная работа 2. Задание №1\nЧетные числа в диапазоне от "a" до "b"')

def  defining_negative_number (s: str) -> int:
    '''Определение отрицательного числа (negative number) и установка флага f=1, если число отрицательное'''
    if (s.startswith('-')) and (s.count('-') == 1) and (s.replace('-', '').isdigit()):
        return 1
    else:
        return 0
        
def exit_while  (s: str, f: int) -> bool:  
    ''' Выход из программы при вводе любой не числовой символ'''
    if not s.isdigit() and f == 0 : 
        return True
    else: False
    
    # Ввод числа и проверка его корректности
def input_number (s: str) -> str:
    a = input(f'Введите первое число "{s}": ') 
    flag = defining_negative_number(a)
    if exit_while(a, flag):
        a = False
    return a

# Бесконечный цикл
while True:

    print('\nДля завершения программы введите любой не числовой символ или число "a" больше или равное "b".\n')

    # Ввод числел с проверкой
    a = input_number('a')
    if a == False: break    
    b = input_number('b')
    if b == False: break
    a, b = int(a), int(b)

    # Выход из программы при вводе числа "a" больше или равное "b"
    if a >= b : break

    # Формирования списка четных чисел в диапазоне от a до b (включительно)
    if (a % 2) == 0:
        my_list = [i for i in range(a,b+1,2)]
    else:
        my_list = [i for i in range(a+1,b+1,2)]

    # Вывод списка четных чисел
    for i in my_list:
        print(i, end=" ")

    # Альтернативный вывод списка четных чисел
    print(f'\n{" ".join(map(str, my_list))}')
    
# Завершение работы программы
print('\n\aПока, пока ...')
