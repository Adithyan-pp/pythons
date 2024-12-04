num1=int(input("enter first number1:"))

num2=int(input("enter second number2:"))

try:
    
    result=num1/num2

    print(result)

except:

    num1=int(input("enter number2"))

    result=num1/num2

    print(result)

finally:

    print("file operation")

    print("db commit")