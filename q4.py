# -*- coding: utf-8 -*-
import turtle
turtle.penup()
turtle.hideturtle()

# Write a new class `Point` with these methods:
# `__init__` sets `self.x` and `self.y`.
# `__str__` returns "(x, y)" for your object's x- and y-coordinates.
# `draw`:
#    1. uses `turtle.goto` to go to that x and y coordinate
#    2. stamps a point with `turtle.dot`

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"{self.x}, {self.y}"
    def draw(self):
        turtle.goto(self.x, self.y)
        turtle.dot()





# Make 4 new objects of the class Point: (0, 0), (100, 0), (100, 100), (0, 100)
# Print your objects.
# Run your draw method for that object.
point1 = Point(0, 0)
point2 = Point(0, 100)
point3 = Point(100, 100)
point4 = Point(100, 0)
print(point1)
print(point2)
print(point3)
print(point4)
point1.draw()
turtle.write(str(point1))
point2.draw()
turtle.write(str(point2))
point3.draw()
turtle.write(str(point3))
point4.draw()
turtle.write(str(point4))



#### OPTIONAL extra credit ####
# The `str` function will run the `__str__` method for an object. Use the
# `turtle.write` method and the `str` function to add a label to your point
# when you draw it.






turtle.exitonclick()

