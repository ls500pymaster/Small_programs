number = int((input("Data: ")))
day = number // (24 * 3600)
hour = (number // 3600) % 24
sec = number % 60
minutes = (number % 3600) // 60

if day % 10 == 1 and day % 100 != 11:
    print(f"{day} День, {hour}:{minutes}:{sec}")
elif 2 <= day % 10 <= 4 and (day % 100 < 10 or day % 100 >= 20):
    print(f"{day} Дня, {hour}:{minutes}:{sec}")
else:
    print(f"{day} Дней, {hour}:{minutes}:{sec}")
