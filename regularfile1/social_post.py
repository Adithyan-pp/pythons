from re import finditer

f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\social_post.txt")

for line in f:

    words=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,words)

    for obj in matcher:

        print(obj.group())


