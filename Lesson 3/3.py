# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    try:
        return sum((a, b, c)) - min(a, b, c)
    except TypeError:
        return "Please enter number!"

print(my_func(8, 9, 2))
