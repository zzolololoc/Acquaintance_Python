"""
Мы работаем в одной небольшой торговой компании,
где все данные о продажах фруктов за год сохранены в словаре в виде пар «название фрукта — доход»:

incomes = {

    'apple': 5600.20,

    'orange': 3500.45,

    'banana': 5000.00,

    'bergamot': 3700.56,

    'durian': 5987.23,

    'grapefruit': 300.40,

    'peach': 10000.50,

    'pear': 1020.00,

    'persimmon': 310.00,

}



В компании наступил небольшой кризис, и нам поручено провести небольшой анализ дохода.

Напишите программу, которая находит общий доход,
затем выводит фрукт с минимальным доходом и удаляет его из словаря. Выведите итоговый словарь на экран.

Результат работы программы:

Общий доход за год составил 35419.34 рублей

Самый маленький доход у grapefruit. Он составляет 300.4 рублей

Итоговый словарь: {'apple': 5600.2, 'orange': 3500.45, 'banana': 5000.0,
'bergamot': 3700.56, 'durian': 5987.23, 'peach': 10000.5, 'pear': 1020.0, 'persimmon': 310.0}


"""


def income_calculation(income_values):
    _total_income = 0
    for _income in income_values:
        _total_income += _income
    return _total_income


def minimum_incomes(incomes):
    _min_incomes_price = max(incomes.values())
    _min_incomes_name = ""
    for name,summ in incomes.items():
        if int(summ) < int(_min_incomes_price):
            _min_incomes_price = summ
            _min_incomes_name = name
    return _min_incomes_price, _min_incomes_name


incomes = {

    'apple': 5600.20,

    'orange': 3500.45,

    'banana': 5000.00,

    'bergamot': 3700.56,

    'durian': 5987.23,

    'grapefruit': 300.40,

    'peach': 10000.50,

    'pear': 1020.00,

    'persimmon': 310.00,

}

print(f"Асортимент продуктов: {incomes}")

income_values = incomes.values()

total_income = income_calculation(income_values)

min_price, min_name = minimum_incomes(incomes)

print(f"Самый маленький доход у {min_name}. Он составляет {min_price} рублей")

incomes.pop(min_name)

print(f"итоговый асортимент: {incomes}")
