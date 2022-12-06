# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

num = int(input('Введите длину: '))
list_num = []
for i in range(num):
    list_num.append(randint(0, 10))
print(list_num)
list_new = []
for i in range(len(list_num)):
    count = 1
    for j in range(i+1, len(list_num)):
        if list_num[j] == list_num[i]:
            count += 1
    for j in range(0, i):
        if list_num[j] == list_num[i]:
            count += 1
    if count == 1:
        list_new.append(list_num[i])
print(list_new)
