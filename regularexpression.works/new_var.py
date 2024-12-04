# enter a number check valid or invalid print valid or invalid

from re import fullmatch

user_input=input("enter the number plate:")

pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,user_input)


if matcher==None:

    print("invalid")

else:

    print("valid")


# PASSPORT
# AADHARw
# LICENSE