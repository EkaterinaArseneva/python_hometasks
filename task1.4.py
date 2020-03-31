"""Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""

user_num = int(input('enter positive number: '))
signs = (len(str(user_num)))
i = 10 ** (signs)
max_num = 0
while i != 0.1:
    i = i / 10
    if i == 0:
        break
    digit = user_num // i
    user_num = user_num % i
    if digit > max_num:
        max_num = digit
print(int(max_num))
