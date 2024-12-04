f1=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\all_students.txt")

f2=open("C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\failed.txt")

all_student_set=set()

failed_student_set=set()

for line in f1:

    line=line.rstrip("\n")

    all_student_set.add(line)

for line in f2:

    line=line.rstrip("\n")

    failed_student_set.add(line)

passed_students=all_student_set.difference(failed_student_set)

print(passed_students)