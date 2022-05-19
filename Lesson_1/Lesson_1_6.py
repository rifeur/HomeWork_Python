dist_start = float(input("Сколько спортсмен пробежал в первый день (в км.): "))
dist_fin = float(input("Какая цель у спортсмена? (в км.): "))
next_day = 0
day_train = dist_start
day = 1
while next_day <= dist_fin:
    next_day = (day_train * 0.1) + day_train
    day_train = next_day
    day = day + 1
print("На", day, "день, спортсмен достиг результата - не менее", dist_fin, "километров")
