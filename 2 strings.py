# Inputs
input_one = input("Please input word: ")
input_two = input("Please input char: ")

first_check = input_one.find(input_two)
if first_check == 0:
    print("None")
else:
    second_check = input_one.find(input_two, first_check+1, len(input_one))
    print(second_check)