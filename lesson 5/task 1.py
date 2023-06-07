numcount = int(input("input count of numbers:\t"))
b = []
c = []
for i in range(numcount):
    a = int(input(f"Input your {i} number:\t"))
    b.append(a)
for i in b:
    c.append(i**2)
print(c)