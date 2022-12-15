# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# def find_txt(text):
#     if 'абв' in text:
#         return False
#     else:
#         True  

txt = open('file01.txt', 'a', encoding = 'utf_8')
text = input('Введите текст: ')
txt.write(text)
txt.close()

txt = open('file01.txt', 'r', encoding = 'utf_8')
find_text = 'абв'
text = txt.read().split()
list_text = [x for x in text if find_text not in x]
print(" ".join(list_text))
txt.close()







