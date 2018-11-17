from pico2d import *
import game_framework


TIME_PER_ACTION = 0.5
FRAME_PER_ACTION = 3.0

ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_TIME = ACTION_PER_TIME * FRAME_PER_ACTION

class UI:
    cur_money_font = None
    rank_font = None

    def __init__(self, x, y, num):
        self.x, self.y = x, y
        self.num = num
        self.frame = 0
        if num == 0:
            self.image = load_image(".\\icons\\GreenUI.png")
            self.character = load_image(".\\character\\Green.png")
        elif num == 1:
            self.image = load_image(".\\icons\\BlueUI.png")
            self.character = load_image(".\\character\\Blue.png")
        if UI.cur_money_font == None:
            UI.cur_money_font = load_font(".\\font\\GodoB.ttf", 20)
        if UI.rank_font == None:
            UI.rank_font = load_font(".\\font\\GodoB.ttf", 20)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)
        self.character.clip_draw(120 * self.frame, 910, 120, 130, self.x-117, self.y, 70, 70)