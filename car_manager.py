import random
from turtle import Turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "white"]

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 1

    def car(self):
        new_car = Turtle()
        new_car.hideturtle()
        new_car.color(random.choice(colors))
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_wid=2, stretch_len=4)

        return new_car

    def set_up(self):
        if random.randint(1, 40) == 1:
            if random.randint(1, 6) == 1:
                car = self.car()
                car.setheading(180)
                car.setpos(SCREEN_WIDTH / 2, (-SCREEN_HEIGHT / 2) + 125)
                car.showturtle()
                self.all_cars.append(car)
            elif random.randint(1, 6) == 2:
                car = self.car()
                car.setpos(-SCREEN_WIDTH / 2, (-SCREEN_HEIGHT / 2) + 175)
                car.showturtle()
                self.all_cars.append(car)
            elif random.randint(1, 6) == 3:
                car = self.car()
                car.setheading(180)
                car.setpos(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 275)
                car.showturtle()
                self.all_cars.append(car)
            elif random.randint(1, 6) == 4:
                car = self.car()
                car.setpos(-SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 225)
                car.showturtle()
                self.all_cars.append(car)
            elif random.randint(1, 6) == 5:
                car = self.car()
                car.setheading(180)
                car.setpos(SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 75)
                car.showturtle()
                self.all_cars.append(car)
            elif random.randint(1, 6) == 6:
                car = self.car()
                car.setpos(-SCREEN_WIDTH / 2, (SCREEN_HEIGHT / 2) - 25)
                car.showturtle()
                self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)