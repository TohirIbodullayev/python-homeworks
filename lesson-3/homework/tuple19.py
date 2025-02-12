tpl = (1, 2, 3, 2, 2, 4)
element = 2
new_tpl = tuple(x for x in tpl if x != element)
print(new_tpl)
