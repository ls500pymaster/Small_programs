# New fun
def calculate_summa(number_one, number_two):
    # Converting list to int
    result = int(''.join(map(str, number_one))) + number_two
    return result

print(calculate_summa(list(input("Number one: ")), int(input("Number two: "))))