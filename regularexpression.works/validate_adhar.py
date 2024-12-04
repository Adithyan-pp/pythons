from re import fullmatch

pancard_number=input("enter pancard number:")

pattern="[A-Z]{3}[PCAFHT][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_number)

if matcher==None:

    print("invalid")

else:

    print("valid")

