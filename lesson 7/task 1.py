mydict = {
    "Variable": "փոփոխական",
    "Declaration": "Հայտարարում",
    "Assignment": "Վերագրում",
    "Data types": "Տվյալների տիպեր",
    "Integer": "Թվային տիպ",
    "String": "Տողային տիպ",
    "Boolean": "Բուլյան տիպ",
    "true": "Ճշմարիտ",
    "else": "Հակառակ դեպքում",
    "array": "Զանգված",
    "if": "Եթե",
    "false": "Կեղծ"
}
a = (input("input word"))
if a in mydict:
   x = mydict.get(a)
   print(x)
else:
    print("Տվյալ բառը բացակայում է բառարանում")