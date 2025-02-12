tpl = (1, 2, 3)
n = 2
repeated_tpl = tuple(x for x in tpl for _ in range(n))
print(repeated_tpl)
