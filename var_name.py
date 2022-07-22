import keyword

str_checker = input("Input: ")
vivod = []
# Lists of ban chars
# spec_char_list = set(r"""`~!@#$%^&*()_-+={[}}|\:;"'<,>.?/""")
keyword_list = keyword.kwlist
# print(spec_char_list)
for i in keyword_list:
    if i in str_checker:
        result_check = False
        break
    else:
        print("can use")