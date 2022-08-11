def difference(*args, **kwargs):
    max_number = max(*args, **kwargs)
    min_number = min(*args, **kwargs)
    result = max_number - min_number
    return ((result.__round__(1)))

print(difference(1, 2, 3))
