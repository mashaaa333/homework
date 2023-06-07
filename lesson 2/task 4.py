a = int (input ("Input number: \t"))
if a % 5 == 0:
    if a % 7 == 0:
        print ("number devides by 5 and 7")
    else:
        print ("number devides by 5")
elif a % 7 == 0:
    print ("number devides by 7")
else:
    print ("no")