from json import load

f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\empolyee.json")

data=load(f)

for emp in data:

    print(emp)