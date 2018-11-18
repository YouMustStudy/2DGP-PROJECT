from pico2d import *
from main_state import CENTER
import math
import game_world
import game_framework

class Building:
    def __init__(self, level, color, tile):
        if level == 0:
            self.x = tile.x
            self.image = Flag(color)
        elif level == 1:
            self.x = tile.x-20
            self.image = House(color)
        elif level == 2:
            self.x = tile.x
            self.image = Condo(color)
        elif level == 3:
            self.x = tile.x+20
            self.image = Hotel(color)

        self.y = tile.y + 100
        self.theta = 0
        self.tile = tile
        self.cur_state = FallenState

    def draw(self):
        self.image.draw(self)

    def update(self):
        self.image.update(self)
        self.cur_state.update(self)

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

class FallenState:
    @staticmethod
    def update(building):
        building.y -= 1000*game_framework.frame_time
        building.y = max(building.tile.y + 50, building.y)
        if building.y == building.tile.y + 50:
            building.cur_state = IdleState

class IdleState:
    @staticmethod
    def update(building):
        pass


class Flag:
    Green = None
    Blue = None

    def __init__(self, color):
        if Flag.Green == None:
            Flag.Green = load_image('.\\building\\GreenFlag.png')
        if Flag.Blue == None:
            Flag.Blue = load_image('.\\building\\BlueFlag.png')
        if color == 0:
            self.image = Flag.Green
        else:
            self.image = Flag.Blue

    def draw(self, building):
        self.image.rotate_draw(math.radians(building.theta), building.x, building.y)

    def update(self, building):
        if building.tile.level != 0:
            game_world.remove_object(building)

class House:
    Green = None
    Blue = None

    def __init__(self, color):
        if House.Green == None:
            House.Green = load_image('.\\building\\GreenHouse.png')
        if House.Blue == None:
            House.Blue = load_image('.\\building\\BlueHouse.png')
        print(color)
        if color == 0:
            self.image = House.Green
        else:
            self.image = House.Blue

    def draw(self, building):
        self.image.rotate_draw(math.radians(building.theta), building.x, building.y)

    def update(self, building):
        pass

class Condo:
    Green = None
    Blue = None

    def __init__(self, color):
        if Condo.Green == None:
            Condo.Green = load_image('.\\building\\GreenCondo.png')
        if Condo.Blue == None:
            Condo.Blue = load_image('.\\building\\BlueCondo.png')
        if color == 0:
            self.image = Condo.Green
        else:
            self.image = Condo.Blue

    def draw(self, building):
        self.image.rotate_draw(math.radians(building.theta), building.x, building.y)

    def update(self, building):
        pass

class Hotel:
    Green = None
    Blue = None

    def __init__(self, color):
        if Hotel.Green == None:
            Hotel.Green = load_image('.\\building\\GreenHotel.png')
        if Hotel.Blue == None:
            Hotel.Blue = load_image('.\\building\\BlueHotel.png')
        if color == 0:
            self.image = Hotel.Green
        else:
            self.image = Hotel.Blue

    def draw(self, building):
        self.image.rotate_draw(math.radians(building.theta), building.x, building.y)

    def update(self, building):
        pass