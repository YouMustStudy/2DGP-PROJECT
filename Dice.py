import math
from Vector import Vector
from pico2d import *
from game_framework import frame_time

#탄성도
elastic = 0.5
#월드의 Z축
axisZ = Vector(0, 0, 1)

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

    def collison_ground(self):
        vecZ = self.vecX.cross(self.vecY)
        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                for k in range(-1, 2, 2):
                    point = Vector(i*self.vecX.x+j*self.vecY.x+k*vecZ.x, i*self.vecX.y+j*self.vecY.y+k*vecZ.y, i*self.vecX.z+j*self.vecY.z+k*vecZ.z)
                    if(self.z + point.z < -1):
                        torque = point.cross(axisZ)
                        torque.normalize()
                        torque.mul( elastic*(max(0, -self.vz) + max(0, self.va.dot(torque.mul(-1)))) + 0.1)
                        self.va.add(torque)


    #피벗을 축으로 회전하는 함수
    def rotate(self, pivot, radian):
        if(radian == 0):
            return None
        piv = pivot.normalize()
        proj = Vector(pivot.x, pivot.y, 0).normalize()
        rotZ = math.acos(proj.x)
        if(proj.y < 0):
            rotZ *= -1
        rotY = math.acos(piv.dot(proj))

        self.vecX.rotateZ(-rotZ).rotateY(-rotY)
        self.vecX.rotateX(radian)
        self.vecX.rotateY(rotY).rotateZ(rotZ)
        self.vecY.rotateZ(-rotZ).rotateY(-rotY)
        self.vecY.rotateX(radian)
        self.vecY.rotateY(rotY).rotateZ(rotZ)

        self.vecX.normalize()
        self.vecY.normalize()