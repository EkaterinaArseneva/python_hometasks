"""Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк. """

time = int(input('enter time in seconds: '))
hh = time // 360
mm = (time % 360) // 60
ss = hh % 60


if len(str(hh)) == 1:
    hh = '0' + str(hh)
if len(str(mm)) == 1:
    mm = '0' + str(mm)
if len(str(ss)) == 1:
    ss = '0' + str(ss)

print(f'{hh}:{mm}:{ss}')
