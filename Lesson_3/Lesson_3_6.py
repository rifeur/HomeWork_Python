def int_func():
    for word in input("Введите слова латинскими маленькимибуквами через пробел: ").split():
        chars = 0
        for char in word:
            if 97 <= ord(char) <= 122:
                chars += 1
        print(word.title() if chars == len(word) else f'{word} - Должно быть только маленькими латинскими буквами.')


int_func()
