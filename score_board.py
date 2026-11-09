from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.level = 1

    def update_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}""\n"f"Score: {self.score}",
                               align="center",
                               font=("Arial", 16, "normal"))