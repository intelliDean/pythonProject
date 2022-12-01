import math


def calculate_diameter(radius):
    return radius * 2


def calculate_circumference(radius):
    return math.pi * 2 * radius


def calculate_area(radius):
    return math.pi * radius * radius


if __name__ == '__main__':
    radius = 3
    print(f"The diameter of the circle is {calculate_diameter(radius):.2f}")
    print(f"The circumference of the circle is {calculate_circumference(radius):.2f}")
    print(f"The area of the circle is {calculate_area(radius):.2f}")

