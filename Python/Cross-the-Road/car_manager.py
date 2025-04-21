from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def createCar(self):
        r = random.randint(1,6)
        if r == 1:
            t = Turtle()
            t.color(random.random(), random.random(), random.random())
            t.shape("square")
            t.shapesize(stretch_wid=1, stretch_len=2, outline=None)
            t.penup()
            t.goto(x=290, y=random.randint(-240,240))
            self.cars.append(t)

    def moveCars(self):
        for c in self.cars:
            c.backward(self.car_speed)

    def levelUp(self):
        self.car_speed += MOVE_INCREMENT


