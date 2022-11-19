# Create Python function drawSquare
# Sara Hernandez
# 11/13/2022
# draw 5 squares

import turtle

def drawSquare(t,sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)

def main():    
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.color("blue")

    size = 20
    
    for i in range(5):
        drawSquare(t,size)
        size = size + 20
        t.penup()
        t.goto(t.pos() + (-10, -10))
        t.pendown()
    wn.mainloop()

 main()



#drawSquare(alex, 20)
#alex.penup()
#alex.goto(0, 0)
#alex.pendown()


#wn.exitonclick()
