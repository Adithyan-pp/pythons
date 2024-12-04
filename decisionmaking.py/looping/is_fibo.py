current=1

is_fibo=False

for i in range(1,number+1):#0 1 1 2 3 5 8 13 21 34 55 89 144 ,,,,,,,,,,

    next=prev+current

    prev=current

    current=next

    if next==number:

        is_fibo=True

        break
