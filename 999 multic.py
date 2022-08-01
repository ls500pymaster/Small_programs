# Number
number = 423
# Tmp var
result = 1
# While loop
while number >= 10:
    result = 1
    # For loop
    for i in range(len(str(number))):
        result *= int(str(number)[i])
    number = result
print(result)
