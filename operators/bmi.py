#BMI=weight_in_kg/(height-in_metre)**2


weight_in_kg=int(input("enter weight in kg:"))

height_in_cm=int(input("enter height in cm:"))

height_in_metre=height_in_cm/100

BMI=weight_in_kg/height_in_metre

BMI=round(BMI)

if BMI<19:

    print("under weight")

elif BMI19<=25:

    print("normal weight")

elif BMI25<30:

    print("over weight")

elif BMI>=30:

    print("obese")
    




