import random
import game_framework
import main_state
import game_world

from Vector import Vector
from pico2d import *
from main_state import CENTER

#탄성도
elastic = 0.6
#월드의 Z축
axisZ = Vector(0, 0, 1)
#60프레임 기준
FRAME_PER_TIME = 60
#경계
BORDER = (400-210+40, 400-210+40, 400+210-40, 400+210-40)

class DiceButton:
    def __init__(self):
        self.image = load_image('.\\icons\\dice.png')
        self.visible = 0
    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.visible * 120, 0, 120, 80, main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2)

    def handle_event(self, event):
        if self.visible == 0 and event.x > main_state.WINDOW_WIDTH/2 - 60 and event.x < main_state.WINDOW_WIDTH/2+60 and event.y > main_state.WINDOW_HEIGHT/2-30 and event.y < main_state.WINDOW_HEIGHT/2+30:
            self.visible = 1
            self.Rolling_Dice()

    def Rolling_Dice(self):
        dice = Dice()
        game_world.add_object(dice, 1)

class Dice:
    image = None
    tick = None
    def __init__(self):
        #주사위의 X, Y 방향 벡터
        self.vecX = Vector(1, 0, 0)
        self.vecY = Vector(0, 1, 0)
        #주사위의 오일러 각
        self.rotX = 0
        self.rotY = 0
        self.rotZ = 0
        #주사위 초기위치
        self.x, self.y = CENTER[0], CENTER[1]
        self.z = 3
        self.oldz = 0
        #주사위 속도
        self.vx = random.randint(-50, +50)
        self.vy = random.randint(-50, +50)
        self.vz = 0
        self.oldvz = 0
        #주사위 각속도
        self.va = Vector(0, 0, 0)
        self.va.normalize()
        self.oldvasize=0
        #주사위 정지 검사
        self.timer = 0.1
        #정지 후 확정 타이머
        self.end = False
        self.endtimer = 1.0
        #주사위 스프라이트
        if Dice.image == None:
            Dice.image = load_image('.\\dice\\dice.png')
        self.index=[0, 0]
        self.rot = 0
        #초기 회전각 부여
        vecDir = Vector(self.vx * 10, self.vy * 10, 0)
        vecDir.normalize()
        vecPivot = vecDir.cross(Vector(0, 0, -1))
        self.rotate(vecPivot, vecPivot.size()*random.randint(20, 130))
        #사운드
        if Dice.tick == None:
            Dice.tick = load_wav('.\\sound\\GameDiceTong14.wav')


    def update(self):
        self.collison_ground()
        self.rotate(self.va, self.va.size() / 10 * game_framework.frame_time * FRAME_PER_TIME)

        if(self.z > 0):
            self.vz -= 3*game_framework.frame_time

        self.x += self.vx * game_framework.frame_time * FRAME_PER_TIME
        self.y += self.vy * game_framework.frame_time * FRAME_PER_TIME
        self.z += self.vz * game_framework.frame_time * FRAME_PER_TIME

        self.x = clamp(BORDER[0], self.x, BORDER[2])
        self.y = clamp(BORDER[1], self.y, BORDER[3])
        self.z = clamp(0, self.z, 10)

        if self.x == BORDER[0] or self.x == BORDER[2]:
            self.vx *= -0.6
        if self.y == BORDER[1] or self.y == BORDER[3]:
            self.vy *= -0.6
        if self.z == 0:
            if self.vz < 0:
                self.vz *= -1
            self.vx *= 0.99
            if math.fabs(self.vx) < 0.01:
                self.vx = 0
            self.vy *= 0.99
            if math.fabs(self.vy) < 0.01:
                self.vy = 0
            self.vz *= 0.8
            if math.fabs(self.vz) < 0.01:
                self.vz = 0
            if self.va.size() < 0.01:
                self.va.set(0, 0, 0)
                self.stablize()

        self.timer -= game_framework.frame_time
        self.timer = max(0, self.timer)
        if self.timer == 0:
            if self.oldz < 0.5 and self.z < 0.5:
                self.z = 0
            if math.fabs(self.oldvz) < 0.5 and math.fabs(self.vz) < 0.5:
                self.vz = 0
            if self.z == 0 and self.oldvasize <0.3 and self.va.size() < 0.3:
                self.va.set(0, 0, 0)
                self.stablize()
                self.end = True
            self.oldz = self.z
            self.oldvz = self.oldvz
            self.oldvasize = self.va.size()
            self.timer = 0.1

        if self.end:
            self.endtimer -= game_framework.frame_time
            if self.endtimer <= 0:
                if self.index[1] == 0:
                    main_state.PLAYER[main_state.PLAYER_TURN].move = 3
                elif self.index[1] == 8:
                    main_state.PLAYER[main_state.PLAYER_TURN].move = 4
                elif self.index[0] == 0:
                    main_state.PLAYER[main_state.PLAYER_TURN].move = 1
                elif self.index[0] == 4:
                    main_state.PLAYER[main_state.PLAYER_TURN].move = 2
                elif self.index[0] == 8:
                    main_state.PLAYER[main_state.PLAYER_TURN].move = 6
                elif self.index[0] == 12:
                    main_state.PLAYER[main_state.PLAYER_TURN].move = 5
                game_world.remove_object(self)


        self.rot = 0
        self.rotX = math.degrees(math.asin(self.vecY.z))
        vecY2 = Vector(self.vecY.x, self.vecY.y, 0)
        vecY2.normalize()
        self.rotZ = math.degrees(math.acos(vecY2.y))
        if vecY2.x > 0:
            self.rotZ *= -1

        cos = vecY2.y
        sin = math.sin(math.radians(self.rotZ))
        vecX2 = Vector(self.vecX.x*cos+self.vecX.y*sin, -self.vecX.x*sin+self.vecX.y*cos, self.vecX.z)

        sin = self.vecY.z
        cos = (1-sin**2)**0.5
        vecX2.set(vecX2.x, vecX2.y*cos+vecX2.z*sin, -vecX2.y*sin+vecX2.z*cos)

        self.rotY = math.degrees(math.acos(vecX2.x))
        if vecX2.z > 0:
            self.rotY *= -1

        self.index[1] = int(self.rotX/22.5 + 4.5)
        self.index[0] = int(-(self.rotY-180)/22.5 + 8.5) % 16

        if self.index[1] == 0 or self.index[1] == 8:
            self.index[0] = 0
        if self.index[1] == 0:
            self.rot = self.rotY
        if self.index[1] == 8:
            self.rot = -self.rotY

        self.rot -= self.rotZ
        self.rot = int(self.rot/22.5 + 0.5) * 22.5


    def draw(self):
        self.image.clip_composite_draw(self.index[0]*46, self.index[1]*46, 46, 46, -math.radians(self.rot), '', self.x, self.y, 1.5*46*(1+self.z/10), 1.5*46*(1+self.z/10))

    def collison_ground(self):
        vecZ = self.vecX.cross(self.vecY)
        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in [-1, 1]:
                    point = Vector(i*self.vecX.x+j*self.vecY.x+k*vecZ.x, i*self.vecX.y+j*self.vecY.y+k*vecZ.y, i*self.vecX.z+j*self.vecY.z+k*vecZ.z)
                    if(self.z + point.z < -1):
                        self.tick.play()
                        torque = point.cross(axisZ)
                        torque.normalize()
                        torque = torque.mul((max(0, -self.vz) + abs(self.va.dot(torque.mul(-1)))) * elastic)
                        self.va = self.va.add(torque)


    #피벗을 축으로 회전하는 함수
    def rotate(self, pivot, radian):
        if(radian == 0):
            return None
        piv = pivot.clone().normalize()
        proj = Vector(pivot.x, pivot.y, 0).normalize()
        rotZ = math.acos(proj.x)
        if(proj.y < 0):
            rotZ *= -1
        rotY = math.acos(clamp(-1, piv.dot(proj), 1))
        self.vecX.rotateZ(-rotZ).rotateY(-rotY)
        self.vecX.rotateX(radian)
        self.vecX.rotateY(rotY).rotateZ(rotZ)

        self.vecY.rotateZ(-rotZ).rotateY(-rotY)
        self.vecY.rotateX(radian)
        self.vecY.rotateY(rotY).rotateZ(rotZ)

        self.vecX.normalize()
        self.vecY.normalize()

    def stablize(self):
        xy = Vector(self.vecX.x, self.vecX.y, 0)
        if math.fabs(self.vecX.z) <= xy.size():
            self.vecX = xy.normalize()
        elif self.vecX.z > 0:
            self.vecX.set(0, 0, 1)
        else:
            self.vecX.set(0, 0, -1)

        xy.set(self.vecY.x, self.vecY.y, 0)
        if math.fabs(self.vecY.z) <= xy.size() and math.fabs(xy.dot(self.vecX)) < 0.01 or self.vecX.z != 0:
            self.vecY = xy.normalize()
        elif self.vecY.z > 0:
            self.vecY.set(0, 0, 1)
        else:
            self.vecY.set(0, 0, -1)