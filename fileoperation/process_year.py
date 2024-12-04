year_path="C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\years.txt"

century_path="C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\century_yr.txt"

leap_year_path="C:\\Users\\adith\\OneDrive\\Desktop\\Pythonworks\\data_set\\leap_yr.txt"

f_read=open(year_path,"r")

f_century=open(century_path,"w")

f_leap_year=open(leap_year_path,"w")

for year in f_read:

    year=int(year)

    if year%100==0:

        f_century.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%100!=0 and year%4==0:

        f_leap_year.write(str(year)+"\n")

f_read.close()

f_century.close()

f_leap_year.close()