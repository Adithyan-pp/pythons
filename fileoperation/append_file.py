f=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\frame_works.txt","a")

frame_works=["wordpress","springboot","oodo","fastapi"]

for fw in frame_works:

    f.write(fw+"\n")

f.close()