from pico2d import *
from random import randint
import game_framework
import game_world

class Dollar:
    image = None
    def __init__(self, x=400, y=400):
        self.dist = randint(200, 400)
        self.length = self.dist / 0.2
        self.x, self.y = x, y + self.dist
        self.timer = 0.5
        if Dollar.image == None:
            Dollar.image = load_image(".\\icons\\dollar.png")

    def update(self):
        length = min(self.dist, self.length * game_framework.frame_time)
        self.dist -= length
        self.y -= length
        if length == 0:
            self.timer -= game_framework.frame_time
            if self.timer <= 0:
                self.x += self.length * game_framework.frame_time
                self.y -= self.length * game_framework.frame_time
        if self.y < 0:
            game_world.remove_object(self)


    def draw(self):
        self.image.draw(self.x, self.y)


class Bundle:
    sound = None
    def __init__(self, x = 400, y = 400):
        self.Dollar = []
        for i in range(3):
            for j in range(5):
                self.Dollar.append(Dollar(x - j * 24 + 48, y - j * 15 + 5*i - 15 + 30))
        for i in range(3):
            for j in range(5-2*i):
                self.Dollar.append(Dollar(x - (j+i) * 24 + 48, y - j * 15 + (-5)*i + 30))
        if Bundle.sound == None:
            Bundle.sound = load_wav('.\\sound\\arrive_other2.wav')
        self.sound.play()


    def update(self):
        for thing in self.Dollar:
            thing.update()
    def draw(self):
        for thing in self.Dollar:
            thing.draw()

def money_ceremony():
    bundle = Bundle()
    game_world.add_object(bundle, 1)