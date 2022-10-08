# <Задание 3>
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов. Если число целое, то его дробная часть не считается за 0 
# и оно (число) в сравнении не участвует.

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19
from random import uniform as uI
from random import randint as rI
from decimal import Decimal

num = int (input('Введите количество чисел в списке: '))
a = int (input('Минимальное число: '))
b = int (input('Максимальное число: '))

arrayFloat = []
for i in range(num):
    coef = rI(1,3)
    num = Decimal(f'{round(uI(a, b), coef)}')
    arrayFloat.append(num)

print(arrayFloat)


