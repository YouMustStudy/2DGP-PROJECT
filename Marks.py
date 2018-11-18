from pico2d import *
import game_framework

class Marks:
    island = None
    tour = None
    olympic = None
    def __init__(self, type):
        if Marks.island == None:
            Marks.island = load_image('.\\icons\\island.png')
        if Marks.tour == None:
            Marks.tour = load_image('.\\icons\\tour.png')
        if Marks.olympic == None:
            Marks.olympic = load_image('.\\icons\\olympic.png')

        if type == 0:
            self.image = Marks.island
        elif type == 1:
            self.image = Marks.tour
        elif type == 2:
            self.image = Marks.olympic

        self.width = self.height = 0
        self.cur_state = EnterState

class EnterState:
    @staticmethod
    def draw(Marks):
        image.draw(400, 400, Marks.width, Marks.height)

    @staticmethod
    def update():
        global width, height, image
        width += image.w * game_framework.frame_time *15
        height += image.h * game_framework.frame_time *15
        width = clamp(0, width, image.w)
        height = clamp(0, height, image.h)
        if width == image.w:
            global cur_state
            cur_state = IdleState