def difference(*args):
    if args == ():
        return ("0")
    max_number = max(*args)
    min_number = min(*args)
    result = max_number - min_number
    return ((result.__round__(1)))


print(difference())
