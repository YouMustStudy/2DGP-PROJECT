from Vector import Vector
from pico2d import *
from game_framework import frame_time

class Dice:
    image = None
    def __init__(self):
        #주사위의 X, Y 방향 벡터
        self.vecX = Vector(1, 0, 0)
        self.vecY = Vector(0, 1, 0)
        #주사위의 오일러 각
        self.rotX = 0
        self.rotY = 0
        self.rotZ = 0
        #주사위 초기위치
        self.x = self.y = 0
        self.z = 0
        #주사위 속도
        self.vx = self.vy = self.vz = 0
        #주사위 각속도
        self.va = Vector(0, 0, 0)
        #주사위 정지 검사
        self.timer = 0.1
        #주사위 스프라이트
        if Dice.image == None:
            Dice.image = load_image('.\\dice\\dice.png')

    def update(self):
        pass

    def draw(self):
        pass