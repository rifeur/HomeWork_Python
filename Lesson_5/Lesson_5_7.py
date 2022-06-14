import json

with open("text_temp_77.json", "w", encoding="UTF-8") as f_json, open("text_7.txt", encoding="UTF-8") as f_txt:
    profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_txt}
    f_up = [i for i in profit.values() if i > 0]
    result = [profit, {"Средний доход фирмы: ": round(sum(f_up) / len(f_up))}]

    json.dump(result, f_json, ensure_ascii=False, indent=4)
