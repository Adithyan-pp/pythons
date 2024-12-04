from re import findall

f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\regularfile1\\sample.txt")

content=f.read()

pattern="https?://[\w\s./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)

    

