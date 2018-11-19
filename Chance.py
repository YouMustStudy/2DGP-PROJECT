from pico2d import *
import game_framework
import game_world
from random import randint

class Chance:
    island = None
    trip = None
    olympic = None

    def __init__(self):
        trigger = randint(0, 3)
        if trigger == 0:
            self.event = None


        self.width = self.height = 0
        self.cur_state = EnterState
        self.timer = 0.8

    def update(self):
        self.cur_state.update(self)

    def draw(self):
        self.cur_state.draw(self)

class EnterState:
    @staticmethod
    def draw(Chance):
        Chance.image.draw(400, 400, Chance.width, Chance.height)

    @staticmethod
    def update(Chance):
        Chance.width += Chance.image.w * game_framework.frame_time *15
        Chance.height += Chance.image.h * game_framework.frame_time *15
        Chance.width = clamp(0, Chance.width, Chance.image.w)
        Chance.height = clamp(0, Chance.height, Chance.image.h)
        if Chance.width == Chance.image.w:
            Chance.cur_state = IdleState

class IdleState:
    @staticmethod
    def draw(Chance):
        Chance.image.draw(400, 400, Chance.width, Chance.height)

    @staticmethod
    def update(Chance):
        Chance.timer -= game_framework.frame_time
        if Chance.timer <= 0:
            Chance.cur_state = ExitState

class ExitState:
    @staticmethod
    def draw(Chance):
        Chance.image.draw(400, 400, Chance.width, Chance.height)

    @staticmethod
    def update(Chance):
        Chance.width -= Chance.image.w * game_framework.frame_time *15
        Chance.height -= Chance.image.h * game_framework.frame_time *15
        Chance.width = clamp(0, Chance.width, Chance.image.w)
        Chance.height = clamp(0, Chance.height, Chance.image.h)
        if Chance.width == 0:
            game_world.remove_object(Chance)

class GotoOlympic:
    image = None
    def __init__(self):
        if GotoOlympic.image == None:
            GotoOlympic.image = load_image(".\\")

    def do(self):


def make_chance():
    tmp = Chance()
    game_world.add_object(tmp, 1)