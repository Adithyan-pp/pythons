age=int(input("enter age:"))
weight=int(input("enter weight:"))
height=int(input("enter height:"))
gender=(input("enter gender:"))

print(weight,height,age,gender)

if gender=="male":
    BMR=10*weight+6.25*height -5*age+5

elif gender=="female":

    BMR=10*weight+6.25*height -5*age-161

else:
    print("*******please enter a vaild number*******")

print(BMR)

activity_level=int(input("""
select activity level
   press 1 for sedentary
   press 2 for lightly active
   press 3 for moderatly active
   press 4 for extra active
   """))
if activity_level==1:
    calorie=BMR*1.2

elif activity_level==2:
    calorie=BMR*1.375
elif activity_level==3:
    calorie=BMR*1.55

elif activity_level==4:
    calorie=BMR*1.9
    

else:
    print("select valid choice for activity level**********")

print(f"total number of  calories you need in order to maintain your current weight={calorie}")

target_weight=int(input("enter weight to  reduce in kg:"))


duration=int(input("enter duration in week:"))

#1kg=>7700



calorie_deficit=target_weight*7700

days=duration*7

daily_calorie_deficit=calorie_deficit/days

print("daily_calorie_deficit",daily_calorie_deficit)




