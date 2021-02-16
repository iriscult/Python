# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать часах * ставка в час) + премия.

from sys import argv

def salary():
    try:
        time, rate, bonus = map(float,argv[1:])
        print(f"Salary - {time * rate +bonus}")
    except ValueError:
        print("Введите три числа")

salary()

