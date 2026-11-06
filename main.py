# Features to Add:
# 1. Figure out how to have the score go up by 1 every time the player moves forward in the game, not just forward.
# 2. Figure out how to implement different levels in a simple way.
# 3. Figure out the car speeds for the different cars in each level.
from turtle import Screen, Turtle
import time
from player import Player
from score_board import ScoreBoard
from car_manager import CarManager

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Main:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Turtle Crossing")

        self.score_board = ScoreBoard()
        self.score_board.goto((SCREEN_WIDTH / -2) + 45, (SCREEN_HEIGHT / 2) - 50)
        self.score_board.write(f"Level: {self.score_board.level}""\n"f"Score: {self.score_board.score}", align="center", font=("Arial", 16, "normal"))

        self.player = Player()
        self.player.hideturtle()
        self.player.sety((SCREEN_HEIGHT/-2) + 50)
        self.player.showturtle()

        self.screen.listen()
        self.screen.onkeypress(self.player.move_up, "Up")
        self.screen.onkeypress(self.player.move_down, "Down")
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.move_right, "Right")

        self.car_manager = CarManager()

        self.is_running = True

    def new_game_setup(self):
        self.screen.clearscreen()

        self.screen.bgcolor("black")

        self.score_board.score = 0
        self.score_board.write(f"{self.score_board.score}", align="center", font=("Arial", 24, "normal"))

        self.player.hideturtle()
        '''self.player.penup()
        self.player.shape("triangle")
        self.player.color("white")'''
        self.player.goto(0, (SCREEN_HEIGHT/-2) + 50)
        self.player.left(90)
        self.player.showturtle()

    def check_play_again(self):
        pass

    def run_game(self):
        while self.is_running:
            self.car_manager.create_car()
            self.car_manager.move_cars()

            time.sleep(0.01)

    def setup_screen(self):
        drawing_pen = Turtle()
        drawing_pen.color("white")
        drawing_pen.speed(0)
        for y in range(int(SCREEN_HEIGHT / -2), SCREEN_HEIGHT + 1, 100):
            drawing_pen.penup()
            drawing_pen.setpos((SCREEN_WIDTH / -2) , y)
            drawing_pen.pendown()
            drawing_pen.goto((SCREEN_WIDTH / 2), y)

if __name__ == '__main__':
    main = Main()
    main.setup_screen()
    main.run_game()
    main.screen.mainloop()