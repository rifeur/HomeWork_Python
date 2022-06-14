dict = {}

with open("text_6.txt", encoding="UTF-8") as my_file:
    for line in my_file:
        name, stats = line.split(':')
        my_sum = sum(map(int, ''.join([i for i in stats if i == ' ' or '9' >= i >= '0']).split()))
        dict[name] = my_sum
    print(f"{dict}")
