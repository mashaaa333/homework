def numsum():
    numbers = input("Enter numbers:\t").split()
    try:
        numbers = [int(num) for num in numbers]
        result = sum(numbers)
        return result
    except ValueError:
        return None
result = numsum()

if result is None:
    print("Error. try again")
else:
    print("Sum of numbers:\t",result)