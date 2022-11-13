# Create Python function flower
# Sara Hernandez
# 11/13/2022
# Use Polygon to create a flower

import turtle

def flower(t,sz):
    for i in range(6):
        t.forward(sz)
        t.left(60)

wn = turtle.Screen()

t = turtle.Turtle()
t.color("palevioletred1")
t.pensize(3)

for j in range(10):
    flower(t,60)
    t.left(36)

wn.exitonclick()