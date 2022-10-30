import string


def InputData(number):
    number = int(input(f'Input number {number}: '))
    return number

def OutputData(number):
    print(f'Число {number}')

def OutputResult(number):
    print(f'Результат операции = {number}')


def InputOperator(charO):
    charO = str(input(f'Input operator {charO}: '))
    return charO