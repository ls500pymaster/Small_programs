new_list = [10.2, -2.2, 0, 1.1, 0.5]
def difference(new_list):
    max_number = max(new_list)
    min_number = min(new_list)
    result = max_number - min_number
    print((result.__round__(1)))

difference(new_list)