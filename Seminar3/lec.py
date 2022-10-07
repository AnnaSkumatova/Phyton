# Задача 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном 
# списке строк некое число.

# num = input("Введите искомое число: ")
# flag = True
# myList = ["gjhgfy54677", "jghgy7546k", "ffytegy543", "jhgdew2135"]

# for element in myList:
#     for charr in element:
#         if num == charr:
#             print("Число присутствует в элементе " + element)
#             flag = False
#             break
# if flag:
#     print("Число не найдено")




# num = input("Введите искомое число: ")
# flag = True
# myList = ["gjhgfy54677", "jghgy7546k", "ffytegy543", "jhgdew2135"]

# for i in range(len(myList)):
#     for charr in myList[i]:
#         if num == charr:
#             print("Число присутствует в элементе с индексом {i} ")
#             flag = False
#             break
# if flag:
#     print("Число не найдено")




# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


from itertools import count


myList = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
num = input("Введите искомое число: ")
buffer = 0
count = 0

for element in range(0, len(myList) - 1):
    if num == myList[element]:
        count +=1
    if count == 2:
        buffer = element
if count == 2:
    print(buffer)
else:
    print("-1")
