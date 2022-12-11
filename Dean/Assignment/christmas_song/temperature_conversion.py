def kelvin_temp(celsius):
    kelvin = celsius + 273.15
    return kelvin


def degree_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


if __name__ == '__main__':
    dc = degree_celsius(float(input("input kelvin to convert to degree celsius\n")))
    print(f"{dc:.2f} degree celsius\n")

    kv = kelvin_temp(float(input("enter degree celsius to convert to kelvin\n")))
    print(f"{kv:.2f} kelvin")
