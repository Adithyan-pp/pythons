f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\names.txt","w")

languages=["python","java","c#","javascript"]

for l in languages:

    f.write(l+"\n")

f.close()