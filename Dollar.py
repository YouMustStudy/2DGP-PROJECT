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
        pass

    def update(self):
        pass

    def draw(self):
        pass