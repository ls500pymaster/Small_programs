import random
# Generate random sets
random_list_one = set(random.sample(range(100), 3))
random_list_two = set(random.sample(range(100), 5))

x = random_list_one
y = random_list_two
# Intersection for 2 sets
z = x.intersection(y)
print(z)
print(x & y)