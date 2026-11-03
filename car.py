from turtle import Turtle

class Car(Turtle):
    def __init__(self):
        self.penup()
        self.shape("square")
        self.showturtle()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.color("blue")