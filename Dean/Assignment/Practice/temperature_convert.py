# convert_cel_to_far() which takes one float parameter representing
# degrees Celsius and returns a float representing the same temperature
# in degrees Fahrenheit using the following formula:
# F = C * 9/5 + 32
def convert_celsius_to_fahrenheit(celsius_int):
    convert = celsius_int * 9 / 5 + 32
    return convert


# convert_far_to_cel() which take one float parameter representing
# degrees Fahrenheit and returns a float representing the same
# temperature in degrees Celsius using the following formula:
# C = (F - 32) * 5/9
def convert_fahrenheit_to_celsius(farh_int):
    convert = (farh_int - 32) * 5 / 9
    return convert


if __name__ == '__main__':
    cel = float(input("Input temperature in celsius\n"))
    far = convert_celsius_to_fahrenheit(cel)
    print(f"{cel} Degree Celsius = {far:.2f} Fahrenheits")


farh = float(input("\nInput temperature in Fahrenheits\n"))
celsius = convert_fahrenheit_to_celsius(farh)
print(f"{far} Fahrenheits = {celsius} Degree Celsius ")


