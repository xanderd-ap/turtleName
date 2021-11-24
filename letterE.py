import turtle
t = turtle.Turtle()
scrn = turtle.Screen()

def drawE(t, size=100):
    t.pendown()
    t.forward(size)
    t.backward(size)
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(size*(7/10))
    t.backward(size*(7/10))
    t.left(90)
    t.forward(60)
    t.right(90)
    t.forward(size)

    turtle.penup()
    turtle.setx(turtle.pos()[0] + size / 2 + size / 40)

if __name__ == "__main__":
    drawE(t)
