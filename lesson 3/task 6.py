n = int(input("input your number:\t"))
f = 1
if n == 0:
    print("factorial of 0 is 1")
else:
    for x in range(1,n + 1):
        f *= x
print("factorial", "of", n, "is", f)
