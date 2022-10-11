# <Задание 5>
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

num = int (input('Введите предел последовательности Фибоначчи: '))

def Fibonachi(num):
    list = [1, 0, 1]
    for i in range(2, num + 1):
        list.append(list[i-1] + list[i])

    for i in range(0, -num + 1, -1):
        list.insert(0, list[1] - list[0])

    return list

print(Fibonachi(num))