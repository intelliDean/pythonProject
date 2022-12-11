def body_mass_index(weight, height):
    KILOGRAMS_PER_POUND = 0.45359237  # Constant

    METERS_PER_INCH = 0.0254  # Constant

    # Compute BMI
    weightInKilograms = weight * KILOGRAMS_PER_POUND

    heightInMeters = height * METERS_PER_INCH

    bmi = weightInKilograms / (heightInMeters * heightInMeters)

    # Display result

    print(f"BMI is {bmi:.2f}")
    if bmi < 18.5:
        return "Underweight"

    elif bmi < 25:
        return "Normal"

    elif bmi < 30:
        return "Overweight"

    else:
        return "Obese"


if __name__ == '__main__':
    weight, height = eval(input("enter weight and height respectively separated by comma\n"))
    result = body_mass_index(weight, height)
    print(result)