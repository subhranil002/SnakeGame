# Imports
from turtle import Turtle
from random import randint


class Food(Turtle):
    # Initializing & Creating Food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.shapesize(stretch_wid=1, stretch_len=1)

    # Food Location Updation
    def refresh(self):
        new_x = randint(-280, 280)
        new_y = randint(-280, 265)

        self.goto(new_x, new_y)

    # To Hide Food
    def hide(self):
        self.hideturtle()

    # To Show Food
    def show(self):
        self.showturtle()


class BigFood(Turtle):
    # Initializing & Creating Big Food
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.hideturtle()

    # To Show Big Food
    def showFood(self):
        new_x = randint(-280, 280)
        new_y = randint(-280, 265)
        self.goto(new_x, new_y)
        self.showturtle()

    # To Hide Big Food
    def hide(self):
        self.hideturtle()

    def show(self):
        self.showturtle()
