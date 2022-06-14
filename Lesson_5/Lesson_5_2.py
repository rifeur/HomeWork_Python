with open("TEXT.txt", encoding='UTF-8') as f:
    res = [f'{count}.{line.strip()} - {len(line.split())} слов(а)' for count, line in enumerate(f, 1)]
    print(*res, f'всего строк - {len(res)}', sep='\n')
