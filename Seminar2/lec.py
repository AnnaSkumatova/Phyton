# Задача 1. Напишите программу, которая принимает на вход число N, и выдает последовательность из N членов.
# пример:
# N = 5: 1, -3, 9, -27, 81 (степени числа -3)

# a = int(input('Input number: '))
# result = []
# for i in range(a):
#     result.append((-3)**i)
# print(result)


# второй вариант
# a = int(input('Input number: '))
# for i in range(a-1):
#     print(pow(-3, i), end=", ")
# print(pow(-3, a-1))




# Задача 2. Для натурального n создать словарь индекс-значениe, состоящий из элементов 
# последовательности 3n + 1
# Example. n = 6:[1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19]


# n = int(input("Введите число: "))

# dict = {}

# for i in range(1, n+1):
#     dict[i] = 3*i+1

# print(dict)




# Задача 3. Напишите программу, в которой пользователь будет задавать две строки, а 
# программа - определять количество вхождений одной строки в другой.

# первый вариант.
# string = "kdjiurgwenrgijwenjfhwenlkorjjwen"
# substring = "wen"

# print(string.count(substring))

# # второй вариант
# string = "kdjiurgwenrgijwenjfhwenlkorjjwen"
# substring = "wen"

# total = 0
# for i in range(len(string)-len(substring)+1):
#     count = 0
#     if string[i] == substring[0]:
#         for j in range(len(substring)):
#             if string[i+j] == substring[j]:
#                 count += 1
#         if count == len(substring):
#             total += 1
# print(f"Строка '{substring}' входит в строку '{string}' - {total} раз(а)")


# третий вариант
string = "kdjiurgwenrgijwenjfhwenlkowenrjjwen"
substring = "wen"

counter = 0

for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        counter +=1
print(f'Количество вхождений - {counter}')


