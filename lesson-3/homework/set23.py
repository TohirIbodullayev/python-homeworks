import random

num_elements = 5 
range_start, range_end = 1, 20

random_set = {random.randint(range_start, range_end) for _ in range(num_elements)}
print(random_set)
