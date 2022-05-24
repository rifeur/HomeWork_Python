my_list = [1, 3.43, 5 + 2j, {1: 'fr', 2: 'ui'}, bytearray(b'yellow'), b'green', {'r', 'e', 'q'}, 'ijefkw', None,
           (6, 4, 2.57),
           ['yaufdh', 3.89, False], False, frozenset(), range(13), zip(*[(1, 2), ('f', 't'), (9, 8)]), TypeError]
for i, sign in enumerate(my_list, 1):
    print(f'{i}) {sign} - {type(sign)}')
