# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input('Введите число ')


def Sum(num):
    sum = 0
    for i in range(len(num)):
        if (num[i] == '-' or num[i] == ',' or num[i] == '.'):
            sum += 0
        else:
            sum += int(num[i])
    return sum


print(Sum(number))
