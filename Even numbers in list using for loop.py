# New list for checking
new_list = [0]
# Plug list
empty_list = []
new_list_even = []
# Plug count
count = 0
# Even
if new_list == []:
    print("0")
else:
    new_list_even = new_list[::2]
    print (new_list)
    # Loop
    for i in new_list_even:
        empty_list.append (i)
        count += i
    last_digit = new_list[-1]
    # Multi all digit and last digit
    mult = count * last_digit
    print (mult)