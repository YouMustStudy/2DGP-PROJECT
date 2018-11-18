from pico2d import *
from main_state import CENTER
import math
import game_world

class Building:
    def __init__(self, level, color, tile):
        if level == 0:
            self.x = tile.x
            self.image = Flag(color)
        elif level == 1:
            self.x = tile.x-20
            self.image = Flag(color)
        elif level == 2:
            self.x = tile.x
            self.image = Flag(color)
        elif level == 3:
            self.x = tile.x+20
            self.image = Flag(color)

        self.y = tile.y + 50
        self.theta = 0
        self.tile = tile

    def draw(self):
        self.image.draw(self)

    def update(self):
        self.image.update(self)

    def rotate(self, theta):
        radian=math.radians(theta)
        self.theta += theta
        if self.theta < 0:
            self.theta = 360+self.theta
        self.x-=CENTER[0]
        self.y-=CENTER[1]
        tmp_x, tmp_y = self.x, self.y
        self.x=tmp_x*math.cos(radian) - tmp_y*math.sin(radian)
        self.y=tmp_x*math.sin(radian) + tmp_y*math.cos(radian)
        self.x+=CENTER[0]
        self.y+=CENTER[1]

class Flag:
    Green = None
    Blue = None

    def __init__(self, color):
        if Flag.Green == None:
            Flag.Green = load_image('.\\building\\GreenFlag.png')
        if Flag.Blue == None:
            Flag.Green = load_image('.\\building\\GreenFlag.png')
        if color == 0:
            self.image = Flag.Green
        else:
            self.image = Flag.Blue

    def draw(self, building):
        self.image.rotate_draw(math.radians(building.theta), building.x, building.y)

    def update(self, building):
        #if building.tile.level != 0:
        #    game_world.remove_object(building)
        pass