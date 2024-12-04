from re import findall

f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\regularfile1\\data.txt")

conent=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=findall(pattern,conent)

for date in dates:

    print(date)
