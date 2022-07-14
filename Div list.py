# Empry list
new_list = []
# Input data
input_string = input("Enter elements of a list separated by space: ")
# Split
user_list = input_string.split()
# Check length of list
len_list = (len(user_list))
# Div list into 2 parts
middle_index = len_list // 2
# Check even or odd
if len_list % 2 == 1:
    first_half = user_list[:middle_index + 1]
    second_half = user_list[middle_index + 1:]
    new_list = [first_half] + [second_half]
    print(new_list)
elif len_list % 2 == 0:
    first_half = user_list[0:middle_index]
    second_half = user_list[middle_index:]
    new_list = [first_half] + [second_half]
    print(new_list)
