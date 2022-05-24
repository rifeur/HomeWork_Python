my_string = input("Введите несколько слов через пробел: ").split()

for i, word in enumerate(my_string, 1):
    print(f'{i}. {word[:10]}')
