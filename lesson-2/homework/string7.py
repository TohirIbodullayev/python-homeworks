a = input("Enter a sentence: ")
b= input("Enter the word to replace: ")
c = input("Enter the replacement word: ")
if b in a:
    upd = a.replace(b, c, 1)
    print("Updated sentence:", upd)