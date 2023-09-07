# Imports
from turtle import Turtle


MESSAGEFONT = ('courier', 30, 'normal')
CONTROLSFONT = ('courier', 26, 'normal')
BACKFONT = ('courier', 14, 'bold')


class onStartup(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()

    def showStartupBorder(self):
        self.color("black")
        self.pensize(5)
        self.goto(-170, 120)
        self.pendown()
        self.goto(170, 120)
        self.goto(170, -70)
        self.goto(-170, -70)
        self.goto(-170, 120)
        self.penup()
        self.color("white")

    def showStartupMessage(self):
        self.color("white")
        self.goto(-140, 50)
        self.write(
            arg="Play (1)", font=MESSAGEFONT)

        self.goto(-140, 0)
        self.write(
            arg="Controls (5)", font=MESSAGEFONT)

        self.goto(-140, -50)
        self.write(
            arg="Exit (0)", font=MESSAGEFONT)

        self.showStartupBorder()

        self.color("yellow")
        self.goto(80, -290)
        self.write(
            arg="Reset High Score(R)", font=BACKFONT)

    def showControls(self):
        self.color("white")
        self.goto(-50, 65)
        self.write(
            arg="Up(W)", font=CONTROLSFONT)

        self.goto(-160, 0)
        self.write(
            arg="Left(A)", font=CONTROLSFONT)

        self.goto(0, 0)
        self.write(
            arg="Right(D)", font=CONTROLSFONT)

        self.goto(-70, -60)
        self.write(
            arg="Down(S)", font=CONTROLSFONT)

        self.showControlsBorder()

        self.color("yellow")
        self.goto(70, -290)
        self.write(
            arg="Back To Main Menu(*)", font=BACKFONT)

    def showControlsBorder(self):
        self.color("black")
        self.pensize(5)
        self.goto(-170, 120)
        self.pendown()
        self.goto(170, 120)
        self.goto(170, -70)
        self.goto(-170, -70)
        self.goto(-170, 120)
        self.penup()
        self.color("white")

    def hideAllMessage(self):
        self.clear()
