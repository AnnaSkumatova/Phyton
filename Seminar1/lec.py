# Задача 1. Напишите программу, которая на вход принимает два числа и проверяет 
# является ли одно число квадратом другого.

# a = int (input('Input first number: '))
# b = int (input('Input second number: '))

# if a == b * b or b == a * a:
#     print('Yes')
# else:
#     print('No')


# a = pow(b, 2) - возводим в степень. b - возводимое число, цифра - степень.
# if a == pow(b, 2) or b == pow(a, 2):




# Задача 2. Напишите программу, которая на вход принимает пять чисел и находит максимальное из них.
# arrayInt = []
# for i in range(5):
#     arrayInt.append(int(input(f'Input {i+1} number: ')))

# maxx = arrayInt[0]
# for i in range(len(arrayInt)):
#     if maxx < arrayInt[i]:
#         maxx = arrayInt[i]
# print(f"Максимальное значение в списке {arrayInt} будет {maxx}")




# Задача 3. Напишите программу которая принимает число n и выводит числа от -n до n

# n = int(input("Input a number: "))
# arrayX = []
# for i in range (-n, n+1):
#     arrayX.append(i)
# print(arrayX)


# Второй вариант
# N = int(input("Input a number: "))

# for i in range(-N, N):
#     print(i, end=', ')
# print(N)


# Задача 4. Напишите программу, которая будет принимать на вход дробь и показывать дпервую цифру дробной части

# x = float(input("Input a number: "))
# if x == int(x):
#     print("Число целое")
# else:
#     print(int((x*10)%10))