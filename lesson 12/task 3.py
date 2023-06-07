num = input("Input your numbers:\t ").split()
num = list(map(int, num))
squared = list(map(lambda x: x**2, num))
print(squared)
