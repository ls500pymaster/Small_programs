# Empty list
new_list = []
# User input
input_string = input("Enter elements of a list separated by space: ")
# Split
input_string = input_string.split()
# Pop last element
new_list_pop = input_string.pop()
# Insert last element
new_list.insert(0, new_list_pop)
# Extend new list
new_list.extend(input_string)
print(new_list)