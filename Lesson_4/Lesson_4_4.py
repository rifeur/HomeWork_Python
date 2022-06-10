from random import randint

rand_list = [randint(-10, 10) for i in range(20)]
ans_list = [i for i in rand_list if rand_list.count(i) == 1]
print(f'{rand_list},\n {ans_list}')
