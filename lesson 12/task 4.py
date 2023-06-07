numbers = input("Input your numbers:\t").split()
numbers = list(map(int, numbers))
answer = lambda nums: [x**2 for x in nums]
result = answer(numbers)
print(result)
