print("Hello. This is Noob Calculator")
# User input
number_1 = int(input("Please input first digit!!!: "))
number_2 = int(input("Please input second digit: "))
# Math action input
math_operation = input("Please select what operation do you want to do: + - / * ")
if math_operation == "/":
    # Checking div by zero
    if not number_1 or number_2 == 0:
        print("Please don't use zero.")
    elif math_operation == "/":
        res_div = int(number_1 / number_2)
        print(res_div)
elif math_operation == "*":
    res_mult = number_1 * number_2
    print (res_mult)
    calc_mode_loop = input("Please ")
    print(calc_mode_loop)
elif math_operation == "+":
    res_add = number_1 + number_2
    print(res_add)
elif math_operation == "-":
    res_sub = number_1 - number_2
    print(res_sub)
else:
    print("Error.")
