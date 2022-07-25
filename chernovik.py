else:
# Check is first elem upper
var_name_checker = "y"
for i in check_var_name:
    if check_var_name.isupper ():
        break
        print ("False")

    else:
        # Check is first elem numeric
        var_name_checker = "y"
        for i in range (len (number_list)):
            first_digit = check_var_name[0]
            if first_digit.isnumeric ():
                break
                print ("False")

            else:
                var_name_checker = "y"
                # Check punctuation
                for i in range (len (punctuation_list)):
                    if check_var_name in punctuation_list:
                        break
                        print ("False")

                    else:
                        var_name_checker = "y"
                        # Check only digits
                        for i in number_list:
                            if check_var_name.isdigit ():
                                break
                                print ("False")
                            else:
                                var_name_checker = "y"
                                # Check keyword list
                                for i in range (0, len (keyword_list)):
                                    if check_var_name in keyword_list:
                                        break
                                        print ("False")

                                    else:
                                        break
                                        print ("True")


                else:
                    # next step
                    for i in range (len (number_list)):
                        first_digit = check_var_name[0]
                        if not first_digit.isnumeric ():
                            var_name_checker = "off"
                            print ("False")
                            break
                        else:
                            # next step
                            # Check punctuation
                            for i in range (len (punctuation_list)):
                                if check_var_name in punctuation_list:
                                    var_name_checker = "off"
                                    print("False")
                                    break