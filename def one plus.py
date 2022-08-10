number_one = [9]
print(type(number_one))
def calculate_summa(number_one):
    # Converting list to int
    number_two = 1
    result = int(''.join(map(str, number_one))) + number_two
    res = [int(x) for x in str(result)]
    return res

print(calculate_summa(number_one))