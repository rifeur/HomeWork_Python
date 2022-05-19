num_sec = int(input("Сколько секунд введем для перевода в привычный формат времени? "))
hour = num_sec // 3600
minutes = num_sec % 3600 // 60
sec = num_sec % 3600 % 60
print("%02d:%02d:%02d" % (hour, minutes, sec))
