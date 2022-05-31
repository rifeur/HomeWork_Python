def sum_func(num_1, num_2, num_3):
    return sum(sorted([num_3, num_2, num_1])[1:])


print(sum_func(4, 2, 6))
