text="malayalam"

length=len(text)-1

reversed=""

for i in range(length,-1,-1):

    reversed+=text[i]

print(reversed)