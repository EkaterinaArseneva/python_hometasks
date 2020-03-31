"""Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = int(input('enter your number '))
nn = int(str(n)*2)
nnn = int(str(n)*3)
result = n + nn + nnn
print(result)