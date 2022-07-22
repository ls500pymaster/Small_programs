import keyword
check_string = input("Type what you want to check: ")
s = keyword.kwlist
print(s)

for i in s:
    if i == check_string:
        print(i)
        break
    else:
        print("Can")