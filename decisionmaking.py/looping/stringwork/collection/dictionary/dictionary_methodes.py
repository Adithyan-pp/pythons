#employee id,name,department,age,salary

employee={"id":42,"name":"adithyan","department":"hr","age":22,"salary":26000}

print(employee.get("salary"))

#pop(key) remove

employee.pop("department")

print(employee)
# return all keys=>keys

for k in employee.keys():

    print(k)

# fetch all values=> values()

for v in employee.values():

    print(v)

# fetch key and values items()

for k,v in   employee.items():

    print(k,v)