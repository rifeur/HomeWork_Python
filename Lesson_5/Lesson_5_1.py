with open("TEXT.txt", 'w', encoding='UTF-8') as f:
    while True:
        line = input("Введите данные построчно, либо введите пустую строку для прекращения операции: ")
        if not line:
            break

        f.write(f'{line}\n')
