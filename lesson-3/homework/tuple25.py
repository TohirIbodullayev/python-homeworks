tpl = (1, 2, 3, 2, 1, 4)
unique_ordered_tpl = []
[unique_ordered_tpl.append(x) for x in tpl if x not in unique_ordered_tpl]
print(tuple(unique_ordered_tpl))
