number=int(input("enter number:"))
orginal=number

digit_count=len(str(number))

total=0

while(number!=0):
    
    digit=number%10

    exponent=digit**digit_count

    total=total+exponent

    number=number//10

print(total)

if total==orginal:
    print("armstrong number")

else:

    print("not armstrong number")