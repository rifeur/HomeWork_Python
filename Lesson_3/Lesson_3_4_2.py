num_1 = float(input("Введите действительное положительное число X: "))
num_2 = int(input("Введите целое отрицательное число Y: "))


def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return "\nНекорректное введение данных\nx должен быть больше 0\ny должен быть меньше 0"
        else:
            res = 1
            for _ in range(abs(y)):
                res /= x
                return f'Число {x}, возведенное в степень {y} равняется:  {round(res, 6)}'
    except ValueError:
        return "Введите корректные данные (числа)"


print(my_func(num_1, num_2))
