from pico2d import *
from random import randint
import game_framework


TIME_PER_ACTION = 1.0
FRAME_PER_ACTION = 3.0

ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_TIME = ACTION_PER_TIME * FRAME_PER_ACTION

class UI:
    money_font = None
    rank_font = None

    def __init__(self, x, y, num, player):
        self.x, self.y = x, y
        self.num = num
        self.frame = randint(1, 2)
        self.player = player
        if num == 0:
            self.image = load_image(".\\icons\\GreenUI.png")
            self.character = load_image(".\\character\\Green.png")
        elif num == 1:
            self.image = load_image(".\\icons\\BlueUI.png")
            self.character = load_image(".\\character\\Blue.png")
        if UI.money_font == None:
            UI.money_font = load_font(".\\font\\GodoB.ttf", 16)
        if UI.rank_font == None:
            UI.rank_font = load_font(".\\font\\GodoB.ttf", 50)

    def update(self):
        self.frame = (self.frame + game_framework.frame_time * FRAME_PER_TIME) % 3

    def draw(self):
        self.image.draw(self.x, self.y)
        self.character.clip_draw(120 * int(self.frame), 910, 120, 130, self.x-117, self.y, 60, 60)
        self.money_font.draw(self.x - 8 * len(str(self.player.cash)) + 40, self.y, str(self.player.cash), (249, 236, 194))
        self.money_font.draw(self.x - 8 * len(str(self.player.money)) + 40, self.y - 30, str(self.player.money), (239, 231, 223))
        self.rank_font.draw(self.x + 95, self.y-3, str(self.player.rank), (239, 231, 223))