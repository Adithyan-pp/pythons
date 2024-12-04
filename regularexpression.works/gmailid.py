#validate gmailid

from re import fullmatch

gmail=input("enter gmail:")

pattern="[a-z]+[a-z0-9]{5,63}@gmail.com"

matcher=fullmatch(pattern,gmail)

if matcher==None:

    print("invalid")

else:

    print("valid")