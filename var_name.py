import string
from keyword import kwlist

# Input
check_var_name = input("Input: ")
keyword_list = kwlist

punctuation_list: str = string.punctuation.replace("_", " ")

loop_exit = True
# While loop

for i in keyword_list:
    if i in check_var_name:
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
