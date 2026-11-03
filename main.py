from turtle import Screen
from player import Player
from car import Car
from score_board import ScoreBoard

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

class Main:
    def __init__(self):
        self.player = Player()

        self.screen = Screen()
        self.screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.screen.bgcolor("black")
        self.screen.title("Turtle Crossing")