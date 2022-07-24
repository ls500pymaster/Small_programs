import keyword
import string
from keyword import kwlist

check_var_name = input ("Input: ")

underline = ["_"]
upper_string = False
number_list = [0, 1, 2, 3, 4, 5]
punctuation_list = ['_', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=',
                    '>', '?', '@', '[', '\\', ']', '^', '`', '{', '|', '}', '~']
del (punctuation_list[0])
print (punctuation_list)
print (underline)
print (type (underline))
print (number_list)
keyword_list = list (kwlist)
print (type (keyword_list))

# Check underline
for i in check_var_name:
    if underline[0] in check_var_name:
        # Check if more __
        if check_var_name.count ('_') >= 2:
            print ("cant 2__ underline")
        break
    else:
        print ("ok")
        break
# Check is first elem upper
for i in check_var_name:
    if check_var_name.isupper () == True:
        print ("cant")
        break
    else:
        print ("ok")
        break
# Check is first elem numeric
for i in range (len (number_list)):
    first_digit = check_var_name[0]
    if first_digit.isnumeric ():
        print ("cant use first digit")
    else:
        print ("can use")
        break
# Check punctuation
for i in range (len (punctuation_list)):
    if check_var_name in punctuation_list:
        print ("cant punct")
        break
    else:
        print ("can punct")
        break
# Check only digits
for i in number_list:
    if check_var_name.isdigit () == True:
        print ("cant use only digits")
    else:
        print ("can use_digit")
        break
# Check keyword list
for i in keyword_list:
    if check_var_name in keyword_list:
        break
        print ("cant use keyword")
    else:
        print ("ok no keyword")
        break
