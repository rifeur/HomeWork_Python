my_list = []
res = [my_list[num] for num in range(1, len(my_list)) if my_list[num] > my_list[num - 1]]
print(res)
