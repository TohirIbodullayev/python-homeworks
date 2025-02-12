lst = [1, 2, 3, 4, 5]
old = 3
new = 9
if old in lst:
    lst[lst.index(old)] = new
print(lst)