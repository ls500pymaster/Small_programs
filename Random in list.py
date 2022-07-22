import random
from random import sample
# Plug new list
new_list = []
# Random count in list
random_number = random.randint(3, 10)
# Generate sample of list in range
sample_list = sample(range(0, 10), random_number)
# Sample
print(sample_list)
# Append digits in new list
new_list.append(list[0])
new_list.append(list[2])
new_list.append(list[-2])
print(new_list)
