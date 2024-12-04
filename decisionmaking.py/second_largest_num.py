num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
num3=int(input("enter third number:"))

if num1>num2 and num1>num3:

    if num2>num3:
        print("num2 is second largest number")

    else:
        print("num3 is second largest number")

elif num2>num1 and num2>num3:
    
    if num1>num3:
        print("num1 is second largest number")

    else:
        print("num3 is second largest")

elif num3>num1 and num3>num2:
    if num1>num2:
        print("num1 is second largest")
    else:
        print("num2 is second largest")

