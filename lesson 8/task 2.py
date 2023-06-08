from random import randint

l = []
l_1 = []
for _ in range(10):
    j = randint(1, 200)
    l.append(j)
for x in l:
    if x % 5 == 0:
        if x > 150:
            continue
        elif x > 500:
            break
        l_1.append(x)

print(l_1)

