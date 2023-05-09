weight_pounds = float(input("Enter your weight in pounds: "))
height_inches = float(input("Enter your height in inches: "))

weight_kg = weight_pounds * 0.45359237
height_meters = height_inches * 0.0254

bmi = weight_kg / (height_meters ** 2)

print("Your BMI is:", int(bmi*10000)/10000)
