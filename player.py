from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        self.penup()
        self.setpos()
        self.shape("triangle")
        self.showturtle()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("white")

    def up(self):
        self.forward(5)