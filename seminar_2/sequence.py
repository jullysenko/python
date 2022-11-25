# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

number = int(input('Введите число '))
list_numbers = []
sum=0
for i in range(1,number+1):
    num =round((1+1/i)**i,2)
    list_numbers.append(num)
    sum=sum+num
print(list_numbers)    
print(sum)

