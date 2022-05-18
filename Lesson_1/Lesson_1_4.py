analys_num = int(input("Введите произвольное положительное целое число для анализа: "))
max_num = 0
while analys_num > 0:
    temp_num = analys_num % 10
    analys_num = analys_num // 10
    if temp_num > max_num:
        max_num = temp_num
print("Наибольшее число в анализируемом, это ", max_num)
