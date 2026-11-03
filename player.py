from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        self.penup()
        self.setpos(270, 270)
        self.shape("triangle")
        self.showturtle()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("white")

    def up(self):
        self.forward(5)

    def down(self):
        self.backward(5)

    def left(self):
        self.left(90)

    def right(self):
        self.right(90)