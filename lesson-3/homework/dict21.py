dct = {"a": 1, "b": 2, "c": 2}
print(dict(sorted(dct.items(), key=lambda x: x[1])))