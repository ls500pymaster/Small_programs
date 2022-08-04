number_one = int(1234)
number_two = int(1)


def calculate_summa(number_one, number_two):
    c = number_one + number_two
    c = str(c)
    result = []
    for char in c:
        result += char
    map_result = list(map(int, result))
    return map_result

print(calculate_summa(number_one, number_two))