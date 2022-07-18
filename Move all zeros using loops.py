new_list = [0, 1, 0, 3, 12]
k = 0
# Loop if i not zero
for i in new_list:
    if i != 0:
        new_list[k] = i
        k += 1
# Replace
for i in range(k, len(new_list)):
    new_list[i] = 0
print(new_list)