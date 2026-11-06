from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("triangle")
        self.color("white")
        self.penup()
        self.left(90)
        self.setx(0)
        self.shapesize(stretch_wid=1, stretch_len=1)

    def move_up(self):
        self.setheading(90)
        self.forward(10)

    def move_down(self):
        self.setheading(270)
        self.forward(10)

    def move_left(self):
        self.setheading(180)
        self.forward(10)

    def move_right(self):
        self.setheading(0)
        self.forward(10)