# Prompt the user to enter weight in pounds
weight = eval(input("Enter weight in pounds\n"))

# Prompt the user to enter height in inches
height = eval(input("Enter height in inches\n"))

KILOGRAMS_PER_POUND = 0.45359237  # Constant
METERS_PER_INCH = 0.0254  # Constant

# Compute BMI
weight_in_kg = weight * KILOGRAMS_PER_POUND
height_in_meters = height * METERS_PER_INCH
bmi = weight_in_kg / (height_in_meters * height_in_meters)

# Display result
print("BMI is", format(bmi, ".2f"))
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
