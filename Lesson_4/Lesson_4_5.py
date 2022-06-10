from functools import reduce

start_list = [i for i in range(100, 1001) if i % 2 == 0]
result = reduce(lambda x, i: x * i, start_list)
print(result)
