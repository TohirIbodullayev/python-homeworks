lst = [1, 2, 3, 2, 1, 4]
unique_ordered_list = []
[unique_ordered_list.append(x) for x in lst if x not in unique_ordered_list]
print(unique_ordered_list)

