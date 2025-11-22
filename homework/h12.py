import turtle
turtle.Screen().bgcolor("pink")
polygon=turtle.Turtle()
num_sides=4
side_length=100
angle=90.0+num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
turtle.done()


