# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'Напишитеабв программу, удалабвяющую из текста всабве слова, содержащие ""абв""'
print(text)
print()

find_text = "абв"
list = [i for i in text.split() if find_text not in i]
print(f'Результат: {" ".join(list)}')