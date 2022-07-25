# Check is first elem upper
for i in check_var_name:
    if check_var_name.isupper ():
        var_name_checker = False
        print ("cant")
        break
    else:
        var_name_checker = True
        print ("ok")
        break
# Check is first elem numeric
for i in range (len (number_list)):
    first_digit = check_var_name[0]
    if first_digit.isnumeric ():
        var_name_checker = False
        print ("cant use first digit")
    else:
        var_name_checker = True
        print ("can use")
        break
# Check punctuation
for i in range (len (punctuation_list)):
    if check_var_name in punctuation_list:
        var_name_checker = False
        print ("cant punct")
        break
    else:
        var_name_checker = True
        print ("can punct")
        break
# Check only digits
for i in number_list:
    if check_var_name.isdigit ():
        var_name_checker = False
        print ("cant use only digits")
    else:
        var_name_checker = True
        print ("can use_digit")
        break
# Check keyword list
for i in keyword_list:
    if check_var_name in keyword_list:
        var_name_checker = False
        break
        print ("cant use keyword")
    else:
        var_name_checker = True
        print ("ok no keyword")
        break
