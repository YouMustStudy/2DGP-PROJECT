from pico2d import *
import game_framework
import game_world
from random import randint

class Chance:
    island = None
    trip = None
    olympic = None

    def __init__(self, player):
        trigger = 2
        if trigger == 0:
            self.event = GotoOlympic()
        if trigger == 1:
            self.event = GotoTrip()
        if trigger == 2:
            self.event = GotoStart()

        self.player = player
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
        Chance.event.image.draw(400, 400, Chance.width, Chance.height)

    @staticmethod
    def update(Chance):
        Chance.width += Chance.event.image.w * game_framework.frame_time *15
        Chance.height += Chance.event.image.h * game_framework.frame_time *15
        Chance.width = clamp(0, Chance.width, Chance.event.image.w)
        Chance.height = clamp(0, Chance.height, Chance.event.image.h)
        if Chance.width == Chance.event.image.w:
            Chance.cur_state = IdleState

class IdleState:
    @staticmethod
    def draw(Chance):
        Chance.event.image.draw(400, 400, Chance.width, Chance.height)

    @staticmethod
    def update(Chance):
        Chance.timer -= game_framework.frame_time
        if Chance.timer <= 0:
            Chance.cur_state = ExitState

class ExitState:
    @staticmethod
    def draw(Chance):
        Chance.event.image.draw(400, 400, Chance.width, Chance.height)

    @staticmethod
    def update(Chance):
        Chance.width -= Chance.event.image.w * game_framework.frame_time *15
        Chance.height -= Chance.event.image.h * game_framework.frame_time *15
        Chance.width = clamp(0, Chance.width, Chance.event.image.w)
        Chance.height = clamp(0, Chance.height, Chance.event.image.h)
        if Chance.width == 0:
            Chance.event.do(Chance)
            game_world.remove_object(Chance)

class GotoOlympic:
    image = None
    def __init__(self):
        if GotoOlympic.image == None:
            GotoOlympic.image = load_image(".\\chance\\olympic.png")

    def do(self, Chance):
        Chance.player.move = 14 - Chance.player.index
        if Chance.player.move < 0:
            Chance.player.move += 28

class GotoTrip:
    image = None
    def __init__(self):
        if GotoTrip.image == None:
            GotoTrip.image = load_image(".\\chance\\trip.png")

    def do(self, Chance):
        Chance.player.move = 21 - Chance.player.index
        if Chance.player.move < 0:
            Chance.player.move += 28

class GotoStart:
    image = None
    def __init__(self):
        if GotoStart.image == None:
            GotoStart.image = load_image(".\\chance\\start.png")

    def do(self, Chance):
        Chance.player.move = 0 - Chance.player.index
        if Chance.player.move < 0:
            Chance.player.move += 28

def make_chance(player):
    tmp = Chance(player)
    game_world.add_object(tmp, 1)