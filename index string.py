# Inputs
input_one = input("Please input word: ")
input_two = input("Please input char: ")

first_check = input_one.find(input_two)
second_check = input_one.find(input_two, first_check+1, len(input_one))

if first_check == -1 or second_check == -1:
    print("None")
else:
    second_check = input_one.find(input_two, first_check+1, len(input_one))
    print(second_check)