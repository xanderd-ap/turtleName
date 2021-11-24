import turtle
t = turtle.Turtle()
scrn = turtle.Screen()

def drawJ(t, size=100, colour="blue"):
    t.pencolor(colour)
    t.pendown()

    turtle.penup()
    turtle.setx(turtle.pos()[0] + size / 2 + size / 40)

if __name__ == "__main__":
    drawJ(t)
