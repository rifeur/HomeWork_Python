my_list = [7, 5, 3, 3, 2]
new_num = ""

while new_num != "q":
    i = 0
    new_num = input("Введите новый элемент рейтинга в форме натурального числа.\nДля выхода - q\n")

    if new_num.isdigit():
        for n in my_list:
            if int(new_num) <= n:
                i += 1
            else:
                break
        my_list.insert(i, int(new_num))
    print(my_list)
