def my_func(x, y):
    try:
        return x ** y
    except TypeError:
        return "Type ERROR"


print(my_func(5, -3))
