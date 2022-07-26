import string
from keyword import kwlist

# Input
check_var_name = input ("Input: ")
keyword_list = kwlist
punctuation_list = string.punctuation.replace ("_", " ")
# Loop exit
loop_exit = True
# While loop
while loop_exit:
    for i in punctuation_list:
        if i not in check_var_name:
            loop_exit = False
            if not check_var_name[0].isdigit ():
                loop_exit = False
                if not check_var_name[0].isnumeric ():
                    loop_exit = False
                    if not check_var_name[0].isupper ():
                        loop_exit = False
                        if not check_var_name in keyword_list:
                            print (loop_exit)
                            break



