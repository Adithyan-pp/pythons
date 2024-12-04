year=int(input("enter year"))

is_non_century_year=year%100!=0

print(is_non_century_year)

if num1>num2 and num1>num3:

    print("num1 is largest")

elif num2>num1 and num2>num3:

    print("num2 is largest")

elif num3>num1 and num3>num2:

    print("num3 is largest")

elif num1==num2 and num2==num3:

    print("all are equal")
    