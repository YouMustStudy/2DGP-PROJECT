from pico2d import*
import main_state
import math


class Bigtile:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.sx, self.sy = x-main_state.WINDOW_WIDTH/2, y-main_state.WINDOW_HEIGHT/2
        self.theta=0
        if Bigtile.image == None:
            Bigtile.image=load_image('Bigtile.png')
            
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


class Smalltile:
    image = None

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.sx, self.sy = x-main_state.WINDOW_WIDTH/2, y-main_state.WINDOW_HEIGHT/2
        self.theta=0
        if Smalltile.image == None:
            Smalltile.image=load_image('Tile.png')
            
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
    tile=load_image('Tile.png')
    bigtile=load_image('Bigtile.png')
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
    return pos


def rotate_world():
    global pos
    for i in range(9):
        clear_canvas()
        for things in pos:
            things.rotate(-10)
            things.draw()
        update_canvas()
        delay(0.03)
    for things in pos:
        things.fix_position()
