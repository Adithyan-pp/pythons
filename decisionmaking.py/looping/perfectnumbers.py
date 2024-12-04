#num
# 1,num 

#write a program to chk number is perfect or not

num=int(input("enter number"))

total=0

for i in range(1,num,1):

    if num%1==0:

        total=total+1

    if num==total:

        print("number is perfect")

    else:

        print("number is not perfect")
        



