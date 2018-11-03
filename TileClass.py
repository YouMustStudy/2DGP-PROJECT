from pico2d import*
import main_state
import math
import json

class Bigtile:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.sx, self.sy = x-main_state.WINDOW_WIDTH/2, y-main_state.WINDOW_HEIGHT/2
        self.theta=0
        self.name=None
        self.image = None
            
    def draw(self):
        self.image.rotate_draw(0, self.x, self.y)

    def update(self):
        pass

    def rotate(self, theta):
        radian=math.radians(theta)
        self.theta += theta
        if self.theta < 0:
            self.theta = 360+self.theta
        self.x-=main_state.WINDOW_WIDTH/2
        self.y-=main_state.WINDOW_HEIGHT/2
        tmp_x, tmp_y = self.x, self.y
        self.x=tmp_x*math.cos(radian) - tmp_y*math.sin(radian)
        self.y=tmp_x*math.sin(radian) + tmp_y*math.cos(radian)
        self.x+=main_state.WINDOW_WIDTH/2
        self.y+=main_state.WINDOW_HEIGHT/2

    def fix_position(self):
        radian = math.radians(self.theta)
        self.x=self.sx*math.cos(radian) - self.sy*math.sin(radian)
        self.y=self.sx*math.sin(radian) + self.sy*math.cos(radian)
        self.x+=main_state.WINDOW_WIDTH/2
        self.y+=main_state.WINDOW_HEIGHT/2

    def fix_start(self):
        self.sx=self.x
        self.sy=self.y


class Smalltile:

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.sx, self.sy = x-main_state.WINDOW_WIDTH/2, y-main_state.WINDOW_HEIGHT/2
        self.theta=0
        self.name=None
        self.image=None
        self.BuildingCost=None
        self.PassingCost=None
        self.level = 0
            
    def draw(self):
        self.image.rotate_draw(math.radians(self.theta), self.x, self.y)

    def update(self):
        pass

    def rotate(self, theta):
        radian=math.radians(theta)
        self.theta += theta
        if self.theta < 0:
            self.theta = 360+self.theta
        self.x-=main_state.WINDOW_WIDTH/2
        self.y-=main_state.WINDOW_HEIGHT/2
        tmp_x, tmp_y = self.x, self.y
        self.x=tmp_x*math.cos(radian) - tmp_y*math.sin(radian)
        self.y=tmp_x*math.sin(radian) + tmp_y*math.cos(radian)
        self.x+=main_state.WINDOW_WIDTH/2
        self.y+=main_state.WINDOW_HEIGHT/2

    def fix_position(self):
        radian = math.radians(self.theta)
        self.x=self.sx*math.cos(radian) - self.sy*math.sin(radian)
        self.y=self.sx*math.sin(radian) + self.sy*math.cos(radian)
        self.x+=main_state.WINDOW_WIDTH/2
        self.y+=main_state.WINDOW_HEIGHT/2

    def fix_start(self):
        self.sx=self.x
        self.sy=self.y

def load_position(x, y):
    pos=[]
    #tile=load_image('Tile.png')
    #bigtile=load_image('Bigtile.png')

    tile=load_image('.\\tile\\방콕.png')
    bigtile=load_image('.\\tile\\무인도.png')

    x-=3*tile.w + bigtile.w/2
    y-=3*tile.w + bigtile.w/2
    pos.append(Bigtile(x, y))
    x+= bigtile.w/2 + tile.w/2
    for i in range(6):
        pos.append(Smalltile(x, y))
        x+=tile.w
    del(tile)
    del(bigtile)
    return pos


def init_tile():
    pos=load_position(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2)
    pos+=load_position(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2)
    for i in range(7):
        pos[-(i+1)].rotate(90)
    pos+=load_position(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2)
    for i in range(7):
        pos[-(i+1)].rotate(180)
    pos+=load_position(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2)
    for i in range(7):
        pos[-(i+1)].rotate(270)

    MAP_DATA_FILE = open('.\\data\\MAP_DATA.txt', 'r')
    MAP_DATA = json.load(MAP_DATA_FILE)
    MAP_DATA_FILE.close()

    for i in range(28):
        pos[i].name = MAP_DATA[str(i)]['Name']
        pos[i].image=load_image('.\\tile\\' + pos[i].name + '.png')
        if (i % 7) != 0:
            pos[i].PassingCost = MAP_DATA[str(i)]['PassingCost']
            pos[i].BuildingCost = MAP_DATA[str(i)]['BuildingCost']

    return pos
