lst = [1, 2, 3, 4, 5]
k = 2
rotated_list = lst[-k:] + lst[:-k]
print(rotated_list)