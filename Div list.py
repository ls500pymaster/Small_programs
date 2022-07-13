# Empry list
new_list = []
# Input data
input_string = input("Enter elements of a list separated by space: ")
# Split
user_list = input_string.split()
# Check length of list
len_list = (len(user_list))
# Div len into 2 parts
len_list_parts = (len_list // 2) + 1
# First and second part of the list
first_half = user_list[:len_list_parts]
second_half = user_list[len_list_parts:]
# Check even or odd
if len_list % 2 == 1:
    new_list = [first_half] + [second_half]
    print(new_list)
else:
    new_list = [first_half] + [second_half]
    print(new_list)