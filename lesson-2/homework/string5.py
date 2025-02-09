a='euioaEUIOA'
b='qwrtypsdfghjklmnbvcxzQWRTYPSDFGHJKLZXCVBNM'
str=input()
cnt1=0
cnt2=0
for i in str:
    if i in a:
        cnt1+=1
    else:
        cnt2+=1
print("Number of wovels: ",cnt1)
print("Number of consonants: ",cnt2)