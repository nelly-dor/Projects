from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-200,260)
        self.level = 1
        self.write(f"Level : {self.level}", move=False, align='center', font=FONT)

    def increaseLevel(self):
        self.level += 1
        self.clear()
        self.write(f"Level : {self.level}", move=False, align='center', font=FONT)

    def endGame(self):
        self.goto(0,0)
        self.write("Game Over", move=False, align='center', font=FONT)

