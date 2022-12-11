import math

x, y, z = 5, 6, "king"
A, B, C = 90, 87, "COME"

f = g = t = "king"

numbers = (5, 6, 5, 3, 5, 3)
cars = ["toyota", "benz", "volvo"]

q, w, r, d, o, p = numbers
p, l, m = cars

ad = "I "
es = "need "
fc = "3k"


# print(ad + es + fc)


def myfunc():
    global x  # any variable created inside a function can only be used in that function,
    # but to be able to use it even outside the function, you declare it with the keyword (global)
    x = "great man"
    # print("i am a", x)


if __name__ == '__main__':
    myfunc()

# print(q)
# print(type(numbers))


import random

i = 1
while i <= 10:
    print(random.randrange(1, 10))  # printing 10 random numbers
    i += 1

radius_int = int(input("enter radius"))  # Thw string captured is cast into int

circumference = 2 * math.pi * radius_int
area = math.pi * radius_int

print("the circumference is:", circumference,
      "\n, and the area is:", area)
