import string
from keyword import kwlist

# Input
check_var_name = input("Input: ")
# Lists
keyword_list = kwlist
punctuation_list: str = string.punctuation.replace("_", " ")
# Exit
loop_exit = True
counter = 0
# if
if check_var_name in keyword_list:
    loop_exit = False
if check_var_name[0].isdigit():
    loop_exit = False
if check_var_name[0].isnumeric():
    loop_exit = False
if check_var_name.count('_') > 1:
    loop_exit = False
for x in check_var_name:
    if x.isupper():
        counter += 1
        loop_exit = False
        break
for p in punctuation_list:
    if p in check_var_name:
        loop_exit = False
        break

print(loop_exit)