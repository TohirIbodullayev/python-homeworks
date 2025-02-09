v='aeiouAEIOU'
s=input()
print("".join('*' if i in v else i for i in s))