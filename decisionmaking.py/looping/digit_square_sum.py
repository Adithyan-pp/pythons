#digit_square_sum

num=int(input("enter number:"))

total=0
while(num!=0):

    digit=num%10

    digit_square=digit**2

    total=total+digit_square

    num=num//10
    
print(total)

