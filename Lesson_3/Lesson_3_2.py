def man_func(**kwargs):
    return " ".join(kwargs.values())


print(man_func(name=input("Введите имя: "), family=input("Введите фамилию: "), date=input("Введите дату рождения: "),
               city=input("Введите свой город: "), email=input("Ведите свой email: "),
               phone_num=input("Введите свой номер телефона: ")))
