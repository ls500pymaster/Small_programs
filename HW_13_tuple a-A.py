import string
string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Input
tuple_input = tuple(input("Please enter: "))
# First letter index
first_letter = tuple_input[0]
# Second letter index
second_letter = tuple_input[-1]
new_list = tuple(string.ascii_letters)

result = (new_list[new_list.index(first_letter):new_list.index(second_letter)+1])
for i in result:
    print(i, end="")
