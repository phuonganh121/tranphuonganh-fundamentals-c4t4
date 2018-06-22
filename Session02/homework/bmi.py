height_in_cm = float(input ("Insert height in cm: "))
height = height_in_cm/100
weight = float(input ("Insert weight in kg: "))

bmi = weight/(height*height) 

print ("BMI = ", bmi)

if bmi < 16:
    print ("Severely underweight")
elif bmi < 18.5:
    print ("Underweight")
elif bmi < 25:
    print ("Normal")
elif bmi < 30:
    print ("Overweight")
else:
    print ("Obese")
