# Features to Add:
# 1. Figure out how to have the score go up by 1 every time the player moves forward in the game, not just forward.
# Figured #1 out, but now I just need to have the y_cor reset after every level, while still updating the score.
# 2. (Like #1) Figure out how to make the player wait if they press a key, and not go continuously forward, going by 1.
# 3. Figure out how to implement different levels in a simple way.
# Figured #2 out, just reuse the same setup layout with the drawing pen, and increase the car speeds.
# 4. Figure out the car speeds for the different cars in each level.
# 5. Ask the player at the start of the game for their time limit, to get the highest score that they can.
# 6. Save that player's score in a file, where a ton of more features can be added onto that.

# Issues to Fix:

from turtle import Screen, Turtle, Terminator
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
        self.score_board.write(f"Level: {self.score_board.level}""\n"f"Score: {self.score_board.score}",
                               align="center",
                               font=("Arial", 16, "normal"))

        self.player = Player()
        self.player.hideturtle()
        self.player.sety((SCREEN_HEIGHT/-2) + 50)
        self.player.showturtle()

        self.drawing_pen = Turtle()
        self.drawing_pen.color("white")
        self.drawing_pen.speed(0)

        self.screen.listen()
        self.screen.onkeypress(self.player.move_up, "Up")
        # self.screen.onkey(self.player.move_up, "Up")
        self.screen.onkeypress(self.player.move_down, "Down")
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.move_right, "Right")

        self.car_manager = CarManager()

        self.is_running = True

    def object_setup(self):
        self.score_board.update_level()

        self.player.hideturtle()
        self.player.setpos(x=0, y=(-SCREEN_HEIGHT / 2) + 50)
        self.player.setheading(90)
        self.player.showturtle()

    def screen_setup(self):
        for y in range(int(SCREEN_HEIGHT / -2), SCREEN_HEIGHT + 1, 100):
            self.drawing_pen.penup()
            self.drawing_pen.setpos((SCREEN_WIDTH / -2) , y)
            self.drawing_pen.pendown()
            self.drawing_pen.goto((SCREEN_WIDTH / 2), y)

    def run_game(self):
        y_cor = self.player.ycor()
        try:
            while self.is_running:

                if self.player.ycor() > y_cor:
                    y_cor = self.player.ycor()
                    self.score_board.update_score()

                if self.player.xcor() >= (SCREEN_WIDTH / 2) - 10:
                    self.player.setx((SCREEN_WIDTH / 2) - 10)
                elif self.player.xcor() <= (-SCREEN_WIDTH / 2) + 5:
                    self.player.setx((-SCREEN_WIDTH / 2) + 5)
                elif self.player.ycor() <= (-SCREEN_HEIGHT / 2) + 10:
                    self.player.sety((-SCREEN_HEIGHT / 2) + 10)
                elif self.player.ycor() >= (SCREEN_HEIGHT / 2):
                    self.level_up()

                self.car_manager.create_car()
                self.car_manager.move_cars()

                time.sleep(0.01)
        except Terminator:
            pass

    def level_up(self):
        self.screen_setup()
        self.object_setup()

    def check_play_again(self):
        pass

if __name__ == '__main__':
    main = Main()
    main.screen_setup()
    main.run_game()
    main.screen.mainloop()