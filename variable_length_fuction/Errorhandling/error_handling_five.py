num1=int(input("enter  first number"))

num2=int(input("enter second number"))

try:
    result=num1/num2

    print(result)#5.0

except Exception as e :

    print(e)

    print("file write")#fw

    print("database commit")#dc