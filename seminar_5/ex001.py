# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# def find_txt(text):
#     if 'абв' in text:
#         return False
#     else:
#         True  

text = input('Введите текст: ')
find_text = 'абв'
text = text.split()
list_text = [x for x in text if find_text not in x]
print(" ".join(list_text))









