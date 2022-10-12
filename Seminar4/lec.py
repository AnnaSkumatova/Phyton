# Задача 1. Создайте в файле, а потом считайте из файла строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

# import random

# size = random.randint(5,10)
# string = ''
# path = r'text.txt'
# pathWrite = r'newtext.txt'

# for _ in range(size):
#     string += f'{random.randint(1,9999)} '

# # print(string[:-1])

# with open(path, 'w', encoding='UTF-8') as data:
#     data.write(string[:-1])

# with open(path, 'r', encoding='UTF-8') as data:
#     data_file = data.readline()

# # print(file)
# file = data_file.split(' ')

# for i in range(len(file)):
#     file[i] = int(file[i])

# print(file)
# result = str(min(file)) + ' => ' + str(max(file))

# with open(pathWrite, 'w', encoding='UTF-8') as data:
#     data.write(data_file + '\n')
#     data.write(result)





# Задача 2. Считайте из файла уравнения Ax^ + Bx + C = 0 и найдите его корни с помощью мат.формул 
# нахождения корней квадратного уравнения



import math
import random
path = 'text_1.txt'
pathWrite = 'solve.txt'


with open(path, 'r', encoding='UTF-8') as data:
    file = data.readline()


data_file = file.replace(' = 0', '').replace(' + ', ' ').replace(' - ', ' -').replace('*x**2', '').replace('*x', '').split()


a = int(data_file[0])
b = int(data_file[1])
c = int(data_file[2])


discr = b**2 - 4*a*c

if discr>0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    result = f'X1 = {x1}, X2 = {x2}'
elif discr ==0:
    x = -b / (2 * a)
    result = f'X = {x}'
else:
    result = 'Корней нет'

with open(path, 'a', encoding='UTF-8') as data:
    data.write('\n' + result)