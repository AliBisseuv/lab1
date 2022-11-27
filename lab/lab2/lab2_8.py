# Инициализация
print('Лабораторная работа 2. Задание №8\nРабота с банковским счетом')
acount = 0.0

def  add_many (s: str) -> None:
    '''Зачисление денег на счет'''
    if s.count(',') == 1:
        s = s.replace(',', '.')
    global acount
    acount += float(s)
    print(f'Зачислено: {float(s):.2f}')
    print(f'На счету: {acount:.2f}')

def sub_many (s: str) -> None:
    '''Снятие денег со счета'''
    if s.count(',') == 1:
        s = s.replace(',', '.')
    global acount
    if acount >= float(s):
        acount -= float(s)
        print(f'Выдано: {float(s):.2f}')
        print(f'Осталось: {acount:.2f}')
        return True
    else:
        print(f'Не достаточно денег на счете.\nСумма на счете: {acount:.2f}')
        return False

def conversy_many () -> None:
    '''Конвертация денег'''
    global acount        
    print(f'\nВыберите операцию с валютой:\n'
            f'1 - USD -> KZT\n'
            f'2 - KZT -> USD\n'
            f'3 - EUR -> KZT\n'
            f'4 - KZT -> EUR')

    oper_operat = input('?> ')
    match oper_operat:
        case '1':           
                print(f'\nСумма до конвертации: {acount:.2f} USD\nСумма после конвертации: {(acount * 470):.2f} KZT')
        case '2':
                print(f'\nСумма до конвертации: {acount:.2f} KZT\nСумма после конвертации: {(acount / 470):.2f} USD')                
        case '3':
                print(f'\nСумма до конвертации: {acount:.2f} EUR\nСумма после конвертации: {(acount * 480):.2f} KZT')
        case '4':
                print(f'\nСумма до конвертации: {acount:.2f} KZT\nСумма после конвертации: {(acount / 480):.2f} EUR')

def  defining_negative_number (s: str) -> int:
    ''' Определение отрицательного числа (negative number) и установка флага f=1, если число отрицательное '''
    if (s.startswith('-')) and (s.coun3t('-') == 1) and (s.replace('-', '').isdigit()):
        f = 1
    elif s.count('.') == 1:
        f = 1
    elif s.count(',') == 1:
        f = 1
    else:
        f = 0
    return f

def exit_while(s: str, f: int) -> bool:
    ''' Выход из программы при вводе любой не числовой символ'''
    if not s.isdigit() and f == 0:
        return True
    else:
        False

def all_correct(a_: str) -> bool:
    flag = defining_negative_number(a_)
    if exit_while(a_, flag):
        a_ = False
    return True
def nul_acount() -> bool:
    global acount
    if acount == 0:
        print(f'На счету нет денег!')
        return False
    else:
        return True

# Бесконечный цикл
while True:

    # Пригласительная строка
    s1 = '1 - пополнение баланса;'
    s2 = '2 - снятие со счета;'
    s3 = '3 - конвертация денег;'
    s4 = '4 - завершение работы.'
    print(f'\nВыберите операцию со счетом:\n{s1}\n{s2}\n{s3}\n{s4}')

    oper_operat_many = input('?> ')
    match oper_operat_many:
        case '1':
            s = input('Введите сумму для внесения на банковский счет: ')
            a = all_correct(s)
            if a == False: break
            add_many(s)
        case '2':
            if nul_acount():
                s = input('Введите сумму для снятия с банковского счета: ')
                a = all_correct(s)
                if a == False: break
                sub_many(s)
        case '3':
            if nul_acount():           
                conversy_many()
        case _:
            break

# Завершение работы программы
print('\n\aПока, пока ...')
