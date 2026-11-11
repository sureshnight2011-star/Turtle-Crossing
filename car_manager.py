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
        if random.randint(1, 5) == 1:
            lane = random.randint(1, 6)

            lane_coordinates = {
                1: ((-SCREEN_HEIGHT / 2) + 125, 180, SCREEN_WIDTH / 2),
                2: ((-SCREEN_HEIGHT / 2) + 175, 0, -SCREEN_WIDTH / 2),
                3: ((SCREEN_HEIGHT / 2) - 275, 180, SCREEN_WIDTH / 2),
                4: ((SCREEN_HEIGHT / 2) - 225, 0, -SCREEN_WIDTH / 2),
                5: ((SCREEN_HEIGHT / 2) - 75, 180, SCREEN_WIDTH / 2),
                6: ((SCREEN_HEIGHT / 2) - 25, 0, -SCREEN_WIDTH / 2),
            }

            if lane in lane_coordinates:
                y_pos, heading, x_pos = lane_coordinates[lane]

                can_spawn = True
                for car in self.all_cars:
                    if abs(car.ycor() - y_pos) < 5:
                        if x_pos > 0 and car.xcor() > x_pos - 120:
                            can_spawn = False
                            break
                        elif x_pos < 0 and car.xcor() < x_pos + 120:
                            can_spawn = False
                            break

                if can_spawn:
                    car = self.car()
                    car.setheading(heading)
                    car.setpos(x_pos, y_pos)
                    car.showturtle()
                    self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def clear_cars(self):
        for car in self.all_cars:
            car.hideturtle()
        self.all_cars.clear()