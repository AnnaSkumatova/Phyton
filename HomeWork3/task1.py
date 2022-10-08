# <Задание 1>
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rI

num = int (input('Введите количество чисел в списке: '))
a = int (input('Минимальное число: '))
b = int (input('Максимальное число: '))

arrayInt = []
for i in range(num):
    arrayInt.append(rI(a, b))

print(arrayInt)

myList = []
for i in range(len(arrayInt)):
    if i % 2 == 1:
        myList.append(arrayInt[i])
print(sum(myList))



# второй вариант:
# newMyList = []
# for i in range(1, len(arrayInt), 2):
#     newMyList.append(arrayInt[i])
# print(sum(newMyList))