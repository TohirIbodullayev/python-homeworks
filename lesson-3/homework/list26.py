lst = [10, 20, 4, 45, 99]
mid = len(lst) // 2
middle = lst[mid] if len(lst) % 2 != 0 else (lst[mid - 1], lst[mid])
print(middle)