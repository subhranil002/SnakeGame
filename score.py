# Imports
from turtle import Turtle


# Constants
ALIGNMENT = "center"
SMALLFONT = ('courier', 14, 'bold')
BIGFONT = ('Roboto', 24, 'bold')


class Score(Turtle):
    # Initializing & Creating Score Board
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("HighScoreDB.txt", mode="r") as file:
            highscore = int(file.read())
        self.highscore = highscore
        self.penup()
        self.hideturtle()

    # To Show Score
    def showScore(self):
        self.color("yellow")
        self.goto(-240, 270)
        self.write(
            arg=f"Score : {self.score}", align=ALIGNMENT, font=SMALLFONT)

        self.goto(200, 270)
        self.write(
            arg=f"High Score : {self.highscore}", align=ALIGNMENT, font=SMALLFONT)

    # To Update Score
    def updateScore(self):
        self.score += 1
        self.clear()
        self.showScore()

    # To Update Extra Score
    def updateExtraScore(self):
        self.score += 21
        self.clear()
        self.showScore()

    # Reset High Score
    def resetHighScore(self):
        with open("HighScoreDB.txt", mode="w") as file:
            file.write("0")
        with open("HighScoreDB.txt", mode="r") as file:
            highscore = int(file.read())
        self.highscore = highscore

    # To Show Game Over & Remember High Score
    def gameOver(self):
        self.clear()
        if self.highscore < self.score:
            with open("HighScoreDB.txt", mode="w") as file:
                file.write(str(self.score))

            self.goto(0, 20)
            self.color("Navy Blue")
            self.write(
                arg=f"New High Score : {self.score}", align=ALIGNMENT, font=BIGFONT)
            self.goto(0, -20)
            self.color("Navy Blue")
            self.write(arg="GAME OVER", align=ALIGNMENT, font=BIGFONT)

        else:
            self.goto(0, 0)
            self.color("Navy Blue")
            self.write(arg="GAME OVER", align=ALIGNMENT, font=BIGFONT)

    def showOnlyHighScore(self):
        with open("HighScoreDB.txt", mode="r") as file:
            highscore = int(file.read())
        self.highscore = highscore
        self.color("yellow")
        self.goto(200, 270)
        self.write(
            arg=f"High Score : {self.highscore}", align=ALIGNMENT, font=SMALLFONT)

    def reset(self):
        self.score = 0

    def hide(self):
        self.clear()
