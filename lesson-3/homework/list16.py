lst=[1,2,4,5,6,7,32,3]
odd_count = sum(1 for x in lst if x % 2 != 0)
print(odd_count)