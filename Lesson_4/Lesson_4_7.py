def fact(num):
    st_num = 1
    for i in range(num + 1):
        yield f'{i}! = {st_num}'
        st_num *= i + 1


for el in fact(int(input('Введите число для нахождения факториала: '))):
    print(el)
