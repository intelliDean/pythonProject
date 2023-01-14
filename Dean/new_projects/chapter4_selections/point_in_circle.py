import turtle

x1, y1 = eval(input("Enter the center of a circle x, y\n"))
radius = eval(input("Enter the radius of the circle\n"))
x2, y2 = eval(input("Enter a point x, y\n"))

# Draw the circle
turtle.penup()  # Pull the pen up
turtle.goto(x1, y1 - radius)
turtle.pendown()  # Pull the pen down
turtle.circle(radius)
# Draw the point
turtle.penup()  # Pull the pen up
turtle.goto(x2, y2)
turtle.pendown()  # Pull the pen down
turtle.begin_fill()  # Begin to fill color in a shape
turtle.color("red")

turtle.end_fill()  # Fill the shape

# Display the status
turtle.penup()  # Pull the pen up
turtle.goto(x1 - 70, y1 - radius - 20)
turtle.pendown()

d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5
if d <= radius:
    turtle.write("The point is inside the circle")
else:
    turtle.write("The point is outside the circle")

turtle.hideturtle()

turtle.done()
