import random
from turtle import Turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "white"]

class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(1, 6) == 1:
            new_car = Turtle()
            new_car.color(random.choice(colors))
            new_car.penup()
            new_car.setheading(180)
            new_car.shape("square")
            new_car.shapesize(stretch_wid=2, stretch_len=4)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(10)