# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

from functools import reduce

number = int(input('Введите число '))
list_numbers = [round((1+1/i)**i,2) for i in range(1,number+1)]
print(list_numbers)  
sum = reduce(lambda x, y: x + y, list_numbers)
print(sum)




