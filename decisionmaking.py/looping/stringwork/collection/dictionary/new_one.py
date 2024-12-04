# create dictionary employee with key eid,name,salary,department,experience

employee={"eid":567,"name":"adithyan","salary":27000,"department":"hr","experience":12}

print(employee["eid"])

#add contact as 43536

employee["contact"]=43536

print(employee)

if employee["experience"]>5:

    employee["salary"]+=10000

else:

    employee["salary"]+=5000

print(employee)

#add role as SDE if exp>5 else add role as JDE

if employee["experience"]>5:
    employee["role"]="SDE"
else:
    employee["role"]="JDE"
print(employee)