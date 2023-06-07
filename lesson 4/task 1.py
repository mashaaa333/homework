a = input("Input your word:\t")
if len(a) % 2 == 0:
    print("Error.Please input another word")

else:
    b = len(a) // 2
    c = a[b-1:b+2]
    print(c)
