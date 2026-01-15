#this is a BMI calculator that uses the height and weight of the person to calculate the BMI
print("Welcome to the BMI Calculator!")
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))   
bmi = weight / (height ** 2)
bmi_rounded = round(bmi)
print("Your BMI is: " + str(bmi_rounded))   