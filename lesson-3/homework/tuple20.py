tpl = (1, 2, 3, 4, 5, 6)
n = 2
nested_tpl = tuple(tpl[i:i+n] for i in range(0, len(tpl), n))
print(nested_tpl)
