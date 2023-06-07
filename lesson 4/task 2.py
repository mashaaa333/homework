a = input("Input your word:\t")
b = a + "ing"
c = a + "ly"
if len(a) < 3:
    print(a)
if a[-3:] == "ing":
   print(c)
else:print(b)