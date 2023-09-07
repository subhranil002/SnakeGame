# Imports
from turtle import Turtle


# Constants
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    # Initialize
    def __init__(self):
        self.snake = []
        self.head = None

    # Create Snake Body
    def createSnake(self):
        x, y = 0, 0
        for i in range(3):
            new_snake_body = Turtle(shape="square")
            new_snake_body.color("yellow")
            new_snake_body.penup()
            new_snake_body.goto(x, y)
            x -= 20
            self.snake.append(new_snake_body)

        self.head = self.snake[0]
        self.head.color("red")

    # To Extend The Snake
    def extendSnake(self):
        new_snake_body = Turtle(shape="square")
        new_snake_body.color("yellow")
        new_snake_body.penup()
        new_snake_body.goto(self.snake[-1].position())
        self.snake.append(new_snake_body)

    # To Move The Snake
    def move(self):
        for segment in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(x=new_x, y=new_y)

        self.head.forward(MOVE_DISTANCE)

    # To Go Right Side
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # To Go Up Side
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # To Go Left Side
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # To Go Down Side
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def hide(self):
        for segment in self.snake:
            segment.hideturtle()

    def reset(self):
        self.snake.clear()
        self.createSnake()
