with open('text_3.txt', 'r', encoding='UTF-8') as f:
    man_dict = {line.split()[0]: float(line.split()[1]) for line in f}
    print(f'Средняя зарплата = {round(sum(man_dict.values())) / len(man_dict)}\n'
          f'Работники с зарплатой менее 20 000 = {[i[0] for i in man_dict.items() if i[1] < 20000]}')
