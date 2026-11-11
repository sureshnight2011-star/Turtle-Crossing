from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 0
        self.level = 1

    def render(self):
        """Helper method to handle the heavy lifting of clearing and writing."""
        self.clear()
        self.write(f"Level: {self.level}""\n"f"Score: {self.score}",
                   align="center",
                   font=("Arial", 16, "normal"))

    def update_level(self):
        self.level += 1
        self.render()

    def update_score(self):
        self.score += 1
        self.render()