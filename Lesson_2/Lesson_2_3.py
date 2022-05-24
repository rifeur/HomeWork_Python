while True:
    num_month = input('Введите номер месяца от 1 до 12: ')
    if num_month.isdigit() and 0 < int(num_month) <= 12:
        season_1 = ["зима", "весна", "лето", "осень", "зима"]
        season_2 = {0: "зима", 1: "весна", 2: "лето", 3: "осень", 4: "зима"}
        print(f'Список сезонов - {season_1[int(num_month) // 3]}\nСловарь сезонов - {season_2[int(num_month) // 3]}\n')
        break
    else:
        print("Ошибка!")
