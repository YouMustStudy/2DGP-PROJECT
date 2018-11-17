from pico2d import *

class Dollar:
    image = None
    def __init__(self, x=400, y=400):
        self.x, self.y = x, y
        if Dollar.image == None:
            Dollar.image = load_image(".\\icons\\dollar.png")

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)


class Bundle:
    def __init__(self):
        self.Dollar = []
        for i in range(3):
            for j in range(5-2*i):
                self.Dollar.append(Dollar(400 - (j+i) * 24, 400 - j * 15 + (-5)*i))

    def update(self):
        pass

    def draw(self):
        for thing in self.Dollar:
            thing.draw()