from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("coral")

def fwd():
    timmy.forward(10)

def left():
    timmy.left(10)

def right():
    timmy.right(10)

def back():
    timmy.back(10)


screen = Screen()
screen.listen()
screen.onkey(key="Up", fun=fwd)
screen.onkey(key="Left", fun=left)
screen.onkey(key="Right", fun=right)
screen.onkey(key="Down", fun=back)
screen.exitonclick()