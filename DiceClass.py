from pico2d import*
import random
import main_state
import game_world
import game_framework

class Dice:
    def __init__(self):
        self.image = load_image('.\\icons\\dice.png')
        self.visible = 0
    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.visible * 120, 0, 120, 80, 400, 400)

    def handle_event(self, event):
        if self.visible == 0 and event.x > 400 - 60 and event.x < 400+60 and event.y > 400-30 and event.y < 400+30:
            self.visible = 1
            self.Rolling_Dice()

    def Rolling_Dice(self):
        dice = DiceResult()
        game_world.add_object(dice, 1)

class DiceResult:
    image = None
    def __init__(self):
        self.x, self.y = 400, 500
        self.number = random.randint(1, 6)
        self.timer = 0.8
        if DiceResult.image == None:
            DiceResult.image = []
            for i in range(6):
                path = '.\\icons\\' + str(i+1) + '.png'
                DiceResult.image.append(load_image(path))

    def update(self):
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            main_state.PLAYER[main_state.PLAYER_TURN].move = self.number
            game_world.remove_object(self)

    def draw(self):
        self.image[self.number-1].draw(self.x, self.y)