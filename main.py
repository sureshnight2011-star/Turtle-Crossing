from turtle import Screen, Turtle
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

    '''def run_game(self):
        while self.is_running:
            pass'''

    def start_game(self):
        self.new_game_setup()

    def setup_screen(self):
        drawing_pen = Turtle()
        drawing_pen.color("white")
        drawing_pen.speed(0)
        '''for x in range(int(SCREEN_WIDTH / -2), SCREEN_WIDTH + 1, 50):
            drawing_pen.penup()
            drawing_pen.setpos(x, (SCREEN_HEIGHT / -2))
            drawing_pen.pendown()
            drawing_pen.goto(x, SCREEN_HEIGHT / 2)'''
        for y in range(int(SCREEN_HEIGHT / -2), SCREEN_HEIGHT + 1, 100):
            drawing_pen.penup()
            drawing_pen.setpos((SCREEN_WIDTH / -2) , y)
            drawing_pen.pendown()
            drawing_pen.goto((SCREEN_WIDTH / 2), y)

if __name__ == '__main__':
    main = Main()
    main.setup_screen()
    # main.new_game_setup()
    main.screen.mainloop()