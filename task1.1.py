"""Поработайте с переменными, создайте несколько, выведите на экран,
запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран."""

string_a = 'new_a'
int_b = 123
float_c = int_b / 1, 5
bool_d = (int_b == float_c)

print(f'your object {string_a} has type {type(string_a)}\n'
      f'your object {int_b} has type {type(int_b)}\n'
      f'your object {float_c} has type {type(float_c)}\n'
      f'your object {bool_d} has type {type(bool_d)}\n')

for i in range(3):
    user_str = input('input text: ')
    user_num = int(input('input number: '))
    print(user_str, user_num)
