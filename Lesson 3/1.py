# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(a, b):
    try:
        return int(a) / int(b)
    except ZeroDivisionError:
        print('Division by zero is forbidden!')
    except ValueError:
        print('Please enter integers!')

print(div(input(), input()))

