from pico2d import*
import random
import main_state
import game_world
import game_framework

class Dice:
    def __init__(self):
        self.image = load_image('.\\icons\\play.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 400, 50, 50)

    def handle_event(self, event):
        if event.x > 400 - 25 and event.x < 400+25 and event.y > 400-25 and event.y < 400+25:
            self.Rolling_Dice()

    def Rolling_Dice(self):
        dice = DiceResult()
        game_world.add_object(dice, 1)

class DiceResult:
    image = None
    def __init__(self):
        self.x, self.y = 400, 500
        self.number = random.randint(1, 6)
        self.timer = 5.0
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