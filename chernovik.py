import string
from keyword import kwlist

# Input
check_var_name = input("Input: ")
# Lists
keyword_list = kwlist
punctuation_list: str = string.punctuation.replace("_", " ")
# Exit
loop_exit = True

# if
if check_var_name in keyword_list:
    loop_exit = False
elif check_var_name[0].isdigit():
    loop_exit = False
elif check_var_name.upper ():
    loop_exit = False
elif check_var_name[0].isnumeric ():
    loop_exit = False
elif check_var_name.count ('_') > 1:
    loop_exit = False
elif check_var_name in punctuation_list:
    loop_exit = False
print(loop_exit)
