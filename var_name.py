import keyword
import string
from keyword import kwlist
# Input
check_var_name = input ("Input: ")
keyword_list = list (kwlist)
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
punctuation_list = ['_', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                    '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']
del (punctuation_list[0])
# Var for checking
loop_exit = "y"
# While loop
while loop_exit == "y":
    for i in check_var_name:
        if check_var_name.count ('_') > 1:
            print("False")
        else:
            break
            loop_exit = "n"
            print("True")



