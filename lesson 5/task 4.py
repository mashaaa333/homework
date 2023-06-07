numcount = int(input("input count of numbers:\t"))
b = []
for i in range(numcount):
    a = int(input(f"Input your {i} number:\t"))
    b.append(a)
print(b)

c = b.index(20)
b.remove(20)
b.insert(c, 200)
print(b)