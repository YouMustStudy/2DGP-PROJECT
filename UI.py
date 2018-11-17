from pico2d import *

class UI:
    cur_money_font = None
    rank_font = None

    def __init__(self, x, y, num):
        self.x, self.y = x, y
        self.num = num
        if num == 0:
            self.image = load_image(".\\icons\\GreenUI.png")
        elif num == 1:
            self.image = load_image(".\\icons\\BlueUI.png")
        if UI.cur_money_font == None:
            UI.cur_money_font = load_font(".\\font\\GodoB.ttf", 20)
        if UI.rank_font == None:
            UI.rank_font = load_font(".\\font\\GodoB.ttf", 20)

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)