def divide():
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return None
a = int(input("Enter number:\t"))
b = int(input("Enter number:\t"))