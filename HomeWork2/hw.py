# Задача 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# n = float(input("Введите вещественное число: "))

# n = str(n)
# summa: int = 0
 
# for digit in n:
#     if digit.isdigit():
#         summa += int(digit)
 
# print("Сумма:", summa)





# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)


# N = int(input('Введите число: '))
# result = 1
# for i in range(1, N+1):
#     result = result * i
#     print(result, end=' ')






# Задача 3. Задайте список из n чисел последовательности (1+1/n)^n
# Выведите на экран саму последовательность и сумму элеементов этой последовательности (для проверки сумма 
# для 4 элементов = 9,06 (примерно))

# N = int(input('Введите число: '))
# result = 1
# res = []
# for i in range(1, N+1):
#     result = (1 + 1/i)**i
#     res.append(result)

# print(res)
# print(sum(res))





# Задача 4. Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, 
# без него) можно (нужно) использовать библиотеку Random

# import random

# list = []
# for _ in range(10):
#     list.append(random.randint(0, 50))
# print ('Оригинальный список: ' + str(list))

# for i in range(len(list)-1):
#     j = random.randint(0, len(list)-1)
#     list[i], list[j] = list[j], list[i]

# print ('Перемешенный список: ' + str(list))
