

def InputData(string: str):
    number = int(input(f'Input {string} number: '))
    return number

def OutputResult(a, b, oper, number):
    print(f'Результат операции {a} {oper} {b} = {number}')

def InputOperator():
    oper= input(f'Input operator: ')
    return oper

def division_by_zero():
    print('Деление на ноль!')

