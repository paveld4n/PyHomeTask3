# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
# неотрицательных чисел. Из всех арифметических операций допускаются
# только +1 и -1. Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4 

def sum_digit(a, b):
    if b == 0:
        return a
    return sum_digit(a + 1, b - 1)

try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
except ValueError:
    print("Формат ввода не соответствует")
else:
    print(f"Возвращенная сумма чисел: {sum_digit(a, b)}")