a = int(input("input first number:\t"))
b = int(input("input second number:\t"))
for i in range(a, b+1):
    if i % 7 == 0:
        print(i)