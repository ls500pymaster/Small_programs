# New list for checking
new_list = [0, 1, 2, 3, 4, 5]
# Plug list
empty_list = []
# Plug count
count = 0
# Plug last digit
last_digit = 0
# Loop
for i in new_list:
    if i % 2 == 0:
        empty_list.append(i)
        last_digit = new_list[-1]
        count += i
# Multi all digit and last digit
mult = count * last_digit
print(mult)