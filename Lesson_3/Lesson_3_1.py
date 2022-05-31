def my_func(first_num, sec_num):
    try:
        res = int(first_num) / int(sec_num)
        return round(res, 3)
    except ZeroDivisionError:
        return "Delenie na nol'!! "
    except ValueError:
        return "Value error"


print(my_func(input("Введите первое число: "), input("Введите второе число: ")))
