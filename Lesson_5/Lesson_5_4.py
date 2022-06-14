rus_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_temp.txt", "w", encoding="UTF-8") as temp_file:
    with open("text_4.txt", encoding="UTF-8") as work_file:
        temp_file.writelines([line.replace(line.split()[0], rus_dict.get(line.split()[0])) for line in work_file])
