from re import fullmatch

year=input("enter number:")

pattern="((18|19)[0-9]{2}|200[0-9]|201[0-9]|202[0-4])"

matcher=fullmatch(pattern,year)

if matcher==None:

    print("invalid")

else:

    print("valid")