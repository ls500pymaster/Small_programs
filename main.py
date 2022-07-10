number = int(input("Input 5 digit number: "))
# Получаю первое число
a1, number = divmod(number, 10000)
# Получаю второе число
a2, number = divmod(number, 1000)
# Получаю третье число
a3, number = divmod(number, 100)
# Получаю четвертое число
a4, number = divmod(number, 10)
print(number * 10000 + a4 * 1000 + a3 * 100 + a2 * 10 + a1 * 1)