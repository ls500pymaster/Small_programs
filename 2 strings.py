# Inputs
input_one = input("Text: ")
input_two = input("Chars: ")

result = []
exists = False
n = 1

# Enum tuple
for index, char in enumerate(input_one):
    if exists:
        if n > len(input_two)-1:
            exists = False
            n = 1
        elif char == input_two[n]:
            n += 1
        elif char != input_two[n]:
            result = result[:-1]
            n = 1
            exists = False
            # Checking chars
    if char == input_two[0] and not exists:
        exists = True
        result.append(index)

# Del first item
del result[0]

if result == []:
    print("None")
# Converting list to str
else:
    print(int(''.join(map(str, result))))