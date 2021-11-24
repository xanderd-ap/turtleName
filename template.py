import turtle # load the turtle module

scrn = turtle.Screen() # Create/obtain the turtle screen object.
bob = turtle.Turtle() # Create a turtle object, that we can use to draw. (I named it bob for some reason.)

bob.forward(50) # move forward 50 pixels
bob.left(90) # turn left 90 degrees
bob.forward(70)

turtle.done() # cleanup
