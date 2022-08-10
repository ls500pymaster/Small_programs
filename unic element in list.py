new_list = input("Input list of nums with spaces: ")
new_list = new_list.split()
empty_list = []
empty_list_2 = []

def unic_num(new_list):
    for num in new_list:
        if new_list.count(num) > 1:
            empty_list.append(num)
        else:
            empty_list_2.append(num)
            return empty_list_2[0]

print(unic_num(new_list))
