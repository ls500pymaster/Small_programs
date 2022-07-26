import string
from keyword import kwlist
# Input
check_var_name = input("Input: ")
keyword_list = kwlist

punctuation_list = string.punctuation.replace("_", " ")

loop_exit = True
# While loop
while loop_exit:
    for i in punctuation_list:
        if i in check_var_name:
            loop_exit = False
            if check_var_name[0].isdigit():
                loop_exit = False

print(loop_exit)