"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

from sys import argv

script_name, working_hours, rate_per_hor, bonus = argv

try:
    print(f'salary is: {int(working_hours)*int(rate_per_hor)+int(bonus)}')
except ValueError:
    print('enter parameters in numbers')