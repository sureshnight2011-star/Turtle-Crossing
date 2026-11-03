from turtle import Screen
from player import Player
from car import Car
from score_board import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Main:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Turtle Crossing")

        self.score_board = ScoreBoard()
        self.score_board.goto((SCREEN_WIDTH / -2) + 25, (SCREEN_HEIGHT / 2) - 50)
        self.score_board.write(f"{self.score_board.score}", align="center", font=("Arial", 24, "normal"))

        self.player = Player()
        self.player.hideturtle()
        self.player.sety((SCREEN_HEIGHT/-2) + 50)
        self.player.showturtle()

        self.screen.listen()
        self.screen.onkeypress(self.player.move_up, "Up")
        self.screen.onkeypress(self.player.move_down, "Down")
        self.screen.onkeypress(self.player.move_left, "Left")
        self.screen.onkeypress(self.player.move_right, "Right")

        self.is_running = True

    def new_game_setup(self):
        self.screen.clear()


    def check_play_again(self):
        pass

    '''def run_game(self):
        while self.is_running:
            pass'''

if __name__ == '__main__':
    main = Main()
    main.screen.mainloop()