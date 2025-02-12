tpl = (1, 2, 3, 2, 2, 4)
element = 2
indices = [i for i, x in enumerate(tpl) if x == element]
print(indices)