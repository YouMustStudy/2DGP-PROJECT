from pico2d import*
import main_state

class Player:
    def __init__(self, x, y, shape):
        self.index=0 #현 위치
        self.x = x
        self.y = y
        self.money=0 #총자산
        self.cash=0 #현자산
        self.image = None
        if shape == 'p':
            self.image = load_image('.\\character\\pig.png')
        elif shape == 's':
            self.image = load_image('.\\character\\skeleton.png')
        self.status = IdleState
        self.frame = 0
        self.move = 0

    def draw(self):
        self.status.draw(self)

    def update(self):
        self.status.do(self)

    def rotate(self, theta):
        theta=math.radians(theta)
        self.x-=main_state.WINDOW_WIDTH/2
        self.y-=main_state.WINDOW_HEIGHT/2
        tmp_x, tmp_y = self.x, self.y
        self.x=tmp_x*math.cos(theta) - tmp_y*math.sin(theta)
        self.y=tmp_x*math.sin(theta) + tmp_y*math.cos(theta)
        self.x+=main_state.WINDOW_WIDTH/2
        self.y+=main_state.WINDOW_HEIGHT/2

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
        if player.move > 0:
            player.change_state(RunState)
    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 20, 0, 20, 20, player.x, player.y)
class RunState:
    @staticmethod
    def enter(player):
        player.frame = 0
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def do(player):
        player.frame = (player.frame+1) % 2
        player.x += 1
        player.x = clamp(main_state.MAP[player.index].x, player.x, main_state.MAP[player.index+1].x)
        if player.x == main_state.MAP[player.index+1].x:
            player.index += 1
            player.move -= 1
            if main_state.MAP[player.index].theta > 0:
                player.change_state(SpinState)
            elif player.move == 0:
                player.change_state(IdleState)


    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 20 + 20, 0, 20, 20, player.x, player.y)
class SpinState:
    @staticmethod
    def enter(player):
        player.frame = 0
    @staticmethod
    def exit(player):
        pass
    @staticmethod
    def do(player):
        player.frame = (player.frame+1) % 2
        if main_state.MAP[player.index].theta > 0:
            player.rotate(-1)
            main_state.rotate_map(-1)
        else:
            main_state.fix_map()
            player.change_state(IdleState)

    @staticmethod
    def draw(player):
        player.image.clip_draw(player.frame * 20 + 20, 0, 20, 20, player.x, player.y)