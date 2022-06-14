from random import randint

with open("text_5.txt", "w", encoding="UTF-8") as work_file:
    my_num = [randint(50, 132) for i in range(20)]
    work_file.write(" ".join(map(str, my_num)))
    with open("text_5.txt", encoding="UTF-8"):
        print(f'Сумма произвольных чисел = {sum(my_num)}')
