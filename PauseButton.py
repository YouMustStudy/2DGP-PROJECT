from pico2d import *
import game_framework
import pause_state

class PurseButton:
    image = None

    def __init__(self):
        if PurseButton.image == None:
            PurseButton.image = load_image('.\\icons\\settings.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(750, 955, 50, 50)

    def handle_events(self, event):
        if event.x > 750 - 25 and event.x < 750 + 25 and event.y > 750 - 25 and event.y < 750 + 25:
            game_framework.push_state(pause_state)