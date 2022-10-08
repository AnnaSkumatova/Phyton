# <Задание 2>
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний 
# элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

from random import randint as rI
from xml.dom.minidom import Element

num = int (input('Введите количество чисел в списке: '))
a = int (input('Минимальное число: '))
b = int (input('Максимальное число: '))

arrayInt = []
for i in range(num):
    arrayInt.append(rI(a, b))

print(arrayInt)

arrLen = num

proizvedenie = []
for i in range(arrLen//2+1):
    Element = arrayInt[i] * arrayInt[arrLen - i - 1]
    proizvedenie.append(Element)

print(proizvedenie)

