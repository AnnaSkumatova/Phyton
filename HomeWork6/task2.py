# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = float(input("Введите вещественное число: "))

def sum_digit(n):
    return sum(map(int, list(str(n).replace('.',''))))

print(n)
print(sum_digit(n))