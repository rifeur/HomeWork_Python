from itertools import cycle, count

my_count = count(5)
my_cycle = cycle('QWERTY')

for i in range(10):
    print('(my_count, my_cycle) = ({}, {}) '.format(next(my_count), next(my_cycle)))
