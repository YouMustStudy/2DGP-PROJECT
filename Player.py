from pico2d import*
from main_state import CENTER
import game_framework
import building_state
import main_state
from Dollar import money_ceremony

SPIN_PER_TIME = 1.5
DEGREE_PER_TIME = SPIN_PER_TIME * 360

#아이들
IDLE_TIME_PER_ACTION = 1.0
IDLE_FRAME_PER_ACTION = 3.0
IDLE_ACTION_PER_TIME = 1.0 / IDLE_TIME_PER_ACTION
IDLE_FRAME_PER_TIME = IDLE_ACTION_PER_TIME * IDLE_FRAME_PER_ACTION

#이동
RUN_TIME_PER_ACTION = 1.0
RUN_FRAME_PER_ACTION = 10.0
RUN_ACTION_PER_TIME = 1.0 / RUN_TIME_PER_ACTION
RUN_FRAME_PER_TIME = RUN_ACTION_PER_TIME * RUN_FRAME_PER_ACTION

class Player:
    def __init__(self, x, y, shape):
        self.index=0 #현 위치
        self.x = x
        self.y = y
        self.money=4000 #총자산
        self.cash=4000 #현자산
        self.image = None
        if shape == 'g':
            self.image = load_image('.\\character\\Green.png')
        elif shape == 'b':
            self.image = load_image('.\\character\\Blue.png')
        self.status = IdleState
        self.frame = 0
        self.move = 0
        self.rank = 1
        self.round = 1 #몇바퀴 돌았는지 | 업그레이드 가능한 건물 종류

    def draw(self):
        self.status.draw(self)

    def update(self):
        self.status.do(self)

    def rotate(self, theta):
        theta=math.radians(theta)
        self.x-=CENTER[0]
        self.y-=CENTER[1]
        tmp_x, tmp_y = self.x, self.y
        self.x=tmp_x*math.cos(theta) - tmp_y*math.sin(theta)
        self.y=tmp_x*math.sin(theta) + tmp_y*math.cos(theta)
        self.x+=CENTER[0]
        self.y+=CENTER[1]

    def change_state(self, state):
        self.status.exit(self)
        self.status = state
        self.status.enter(self)

class IdleState:
    @staticmethod
    def enter(player):
        player.frame = 0
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def do(player):
        player.frame = (player.frame + game_framework.frame_time * IDLE_FRAME_PER_TIME) % 3
        if player.move > 0:
            player.change_state(RunState)
    @staticmethod
    def draw(player):
        player.image.clip_draw(120 * int(player.frame), 910, 120, 130, player.x, player.y, 60, 60)

class RunState:
    @staticmethod
    def enter(player):
        player.frame = 0
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def do(player):
        player.frame = (player.frame + game_framework.frame_time * RUN_FRAME_PER_TIME) % 10
        player.x += game_framework.frame_time * 70 * 3
        player.x = clamp(main_state.MAP[player.index].x, player.x, main_state.MAP[(player.index+1)%28].x)
        if player.x == main_state.MAP[(player.index+1)%28].x:
            player.index = (player.index + 1) % 28
            player.move -= 1
            #월급 시스템 추가
            if(player.index == 0):
                player.cash += 600
                player.money += 600
                player.round += 1
                money_ceremony()
            if main_state.MAP[player.index].theta > 0:
                player.change_state(SpinState)
            if player.move == 0:
                player.change_state(IdleState)
                #도착 후 이벤트 처리
                if(player.index % 7 == 0): #큰타일 - 특수이벤트
                    pass
                elif(player.index == 9 or player.index == 24): #찬스카드
                    pass
                elif(main_state.MAP[player.index].owner == -1 or main_state.MAP[player.index].owner == main_state.PLAYER_TURN and main_state.MAP[player.index].level != 3 and main_state.MAP[player.index].return_building() < player.cash): #땅주인이 없거나 본인이 주인이면
                    game_framework.push_state(building_state) #건설상태로 분기
                    return
                else:
                    money_ceremony()
                    main_state.trade_money()
                #이벤트 처리 후 순위 체크
                main_state.check_rank()
                main_state.change_turn()


    @staticmethod
    def draw(player):
        player.image.clip_draw(120 * int(player.frame), 0, 120, 130, player.x, player.y, 60, 60)
class SpinState:
    @staticmethod
    def enter(player):
        player.frame = 0
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def do(player):
        player.frame = (player.frame + game_framework.frame_time * RUN_FRAME_PER_TIME) % 10
        if main_state.MAP[player.index].theta > 0:
            theta = min(main_state.MAP[player.index].theta, DEGREE_PER_TIME * game_framework.frame_time)
            main_state.rotate_world(theta)
        else:
            main_state.fix_map()
            player.change_state(IdleState)

    @staticmethod
    def draw(player):
        player.image.clip_draw(120 * int(player.frame), 0, 120, 130, player.x, player.y, 60, 60)