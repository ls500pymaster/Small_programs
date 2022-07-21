# New list for checking
new_lst = [0]
# Plug list
empty_lst = []
new_lst_even = []
# Plug count
count = 0
# Check for zero
if new_lst == []:
    print("0")
else:
    new_lst_even = new_lst[::2]
    print (new_lst)
    # Loop
    for i in new_lst_even:
        empty_lst.append (i)
        count += i
    last_digit = new_lst[-1]
    # Multi all digit and last digit
    mult = count * last_digit
    print (mult)