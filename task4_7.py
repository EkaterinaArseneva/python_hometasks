"""Реализовать генератор с помощью функции с ключевым словом yield,
создающим очередное значение. При вызове функции должен создаваться объект-генератор.
Функция должна вызываться следующим образом: for el in fact(n). Функция отвечает за получение факториала числа,
а в цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
"""
from functools import reduce

# вариант 1. факториал - это число, поэтому функция генерирует число
def fact(n):
    fact_list = [el for el in range(1, n + 1)]
    factorial = reduce(lambda x, y: x * y, fact_list)
    yield factorial


n = int(input('enter number: '))
for el in fact(n): #и т.к. факториал - это число, в моем объекте только один элемент.
    print(el)

# вариант 2. Пусть тогда мы будем генерировать факториал для каждого числа от 1 до n и выводить в цикле факториалы для
#каждого числа от 1 до n. Но это тоже не по условию задачи.

def fact_2(n):
    fact_list = [el for el in range(1, n + 1)]
    print(fact_list)
    for el in fact_list:
        fact_list_subt = fact_list[0: fact_list.index(el)+1]
        factorial = reduce(lambda x, y: x * y, fact_list_subt)
        yield factorial


for el in fact_2(n):
    print(el)
