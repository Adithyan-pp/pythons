f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\fruits.txt")
fruits=[]
for line in f:

    fruits.append(line.rstrip("\n"))
print(fruits)