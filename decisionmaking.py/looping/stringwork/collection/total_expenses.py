#total expenses

expenses=[12000,13000,14000,11000]
total=0

for exp in expenses:

    total+=exp

print(total)

#max_expense without using max()

expenses=[11000,13000,14000,15000]

gratest=expenses[0]

for exp in expenses:

    max=gratest if gratest else exp

print(max)
#
expenses=[11000,12000,13000,14000]

max_exp=0

for exp in expenses:
    if exp>max_exp:
        max_exp=exp

print(max_exp)

#min_expenses