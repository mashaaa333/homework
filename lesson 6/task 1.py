a = []
for numbers in range(10):
    x = int(input("input number for first list"))
    a.append(x)

b = []
for numbers in range(10):
    y = int(input("input number for second list"))
    b.append(y)

a_set = set(a)
print(a_set)
b_set = set(b)
print(b_set)
print("A = B is", (a_set == b_set))
print("A U B", (a_set.union(b_set)))
print("A ∩ B", (a_set.intersection(b_set)))
print("A difference", (a_set.difference(b_set)))
print("B difference", (b_set.difference(a_set)))