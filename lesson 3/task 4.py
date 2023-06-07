a = 100
for a in range(100,600):
    if a % 3 == 0:
        if a % 11 == 0:
            print(a)
            if a % 7 == 0:
                break