# New fun
def calculate_summa(number_one, number_two):
    # Converting list to int
    result = int(''.join(map(str, number_one))) + number_two
    res = [int(x) for x in str(result)]
    return res

print(calculate_summa(list(input("Number one: ")), int(input("Number two: "))))