from pico2d import *
import game_framework
import game_world

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
        self.timer = 0.5

    def update(self):
        self.cur_state.update(self)

    def draw(self):
        self.cur_state.draw(self)

class EnterState:
    @staticmethod
    def draw(Marks):
        Marks.image.draw(400, 400, Marks.width, Marks.height)

    @staticmethod
    def update(Marks):
        Marks.width += Marks.image.w * game_framework.frame_time *15
        Marks.height += Marks.image.h * game_framework.frame_time *15
        Marks.width = clamp(0, Marks.width, Marks.image.w)
        Marks.height = clamp(0, Marks.height, Marks.image.h)
        if Marks.width == Marks.image.w:
            Marks.cur_state = IdleState

class IdleState:
    @staticmethod
    def draw(Marks):
        Marks.image.draw(400, 400, Marks.width, Marks.height)

    @staticmethod
    def update(Marks):
        Marks.timer -= game_framework.frame_time
        if Marks.timer <= 0:
            Marks.cur_state = ExitState

class ExitState:
    @staticmethod
    def draw(Marks):
        Marks.image.draw(400, 400, Marks.width, Marks.height)

    @staticmethod
    def update(Marks):
        Marks.width += Marks.image.w * game_framework.frame_time *15
        Marks.height += Marks.image.h * game_framework.frame_time *15
        Marks.width = clamp(0, Marks.width, Marks.image.w)
        Marks.height = clamp(0, Marks.height, Marks.image.h)
        if Marks.width == Marks.image.w:
            game_world.remove_object(Marks)