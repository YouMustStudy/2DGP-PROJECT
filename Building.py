from pico2d import *

class Building:
    Bflag = None
    Bhouse = None
    Bcondo = None
    Bhotel = None

    def __init__(self):
        if Building.Bflag == None:
            Building.Bflag = load_image(".\\building\\BlueFlag.png")
        if Building.Bhouse == None:
            Building.Bhouse = load_image(".\\building\\BlueHouse.png")
        if Building.Bcondo == None:
            Building.Bcondo = load_image(".\\building\\BlueCondo.png")
        if Building.Bhotel == None:
            Building.Bhotel = load_image(".\\building\\BlueHotel.png")

    def draw(self):
        pass

    def update(self):
        pass