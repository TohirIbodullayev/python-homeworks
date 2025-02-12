dct = {"a": {"x": 1}, "b": 2}
print(any(isinstance(v, dict) for v in dct.values()))
