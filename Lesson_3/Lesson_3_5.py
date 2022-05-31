def sum_func():
    summ = 0
    while True:
        err = False
        my_list = input("Введите число, или 'q' для выхода: ").split()
        for num in my_list:
            if num.lower() == "q":
                return summ
            else:
                try:
                    summ += int(num)
                except ValueError:
                    err = True
        if err:
            print("Данные не верны")
        print(f"Сумма чисел = {summ}")


print(sum_func())
