"""Запросите у пользователя значения выручки и издержек фирмы.
 Определите, с каким финансовым результатом работает фирма
 (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
 Выведите соответствующее сообщение. Если фирма отработала с прибылью,
 вычислите рентабельность выручки (соотношение прибыли к выручке).
 Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
income = int(input('enter your income: '))
costs = int(input('enter your costs: '))
if income > costs:
    profit = income - costs
    print(f'your profit is :{profit}')
    profitability = profit / income
    print("your profitability is: {:.2f}%".format(profitability*100))
    employees = int(input('enter a number of your employees: '))
    profit_per_employee = profit / employees
    print ("your profit per employee is: {:.0f}".format(profit_per_employee))
else:
    losses = -(income-costs)
    print(f'your losses are :{losses}')
