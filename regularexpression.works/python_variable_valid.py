# variable validation check enter variable is valid or invalid and print valid or invalid

from re import fullmatch

user_input=input("enter the name:")

pattern="[a-zA-Z][a-zA-Z0-9_]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:

    print("invalid")

else:

    print("valid")