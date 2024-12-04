from re import fullmatch

date=input("enter number:")

pattern="(0?[1-9]|[12][0-9]|3[01])"

matcher=fullmatch(pattern,date)

if matcher==None:

    print("invalid")

else:

    print("valid")