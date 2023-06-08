from random import randint
l = []
i = 1
for i in range(10):
    j = randint(-100, 100)
    l.append(j)
print(l)

count = 0
for num in l:
    count += 1

print("Total count:", count)
