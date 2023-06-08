a = int(input("Input your number:\t"))
count = 0
if a == 0:
    print("The number of digits is 1")
while a != 0:
    count += 1
    a //= 10

print("The number of digits is:", count)