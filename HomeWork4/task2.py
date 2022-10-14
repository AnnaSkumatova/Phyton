# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))

devList = []

dev = 2
while num> 2:
    if num%dev != 0:
        dev += 1
    else:
        num //= dev
        devList.append(dev)

print(set(devList))


