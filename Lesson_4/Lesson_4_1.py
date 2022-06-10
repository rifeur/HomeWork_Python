from sys import argv


def sal():
    try:
        hour, cash_hour, bonus = map(float, argv[1:])
        print(f'Зарплата = {hour * cash_hour + bonus}')
    except ValueError:
        print("вводите только числа!")


sal()
