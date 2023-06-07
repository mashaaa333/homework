numcount = int(input("input count of numbers:\t"))
b = []

for i in range(numcount):
    a = int(input(f"Input your {i} number:\t"))
    b.append(a)
print(b)
c = 1
for i in b:
   c *= i
print(c)