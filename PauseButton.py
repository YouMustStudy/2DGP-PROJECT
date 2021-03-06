from pico2d import *
import game_framework
import pause_state

class PauseButton:
    image = None

    def __init__(self):
        if PauseButton.image == None:
            PauseButton.image = load_image('.\\icons\\settings.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(750, 755, 50, 50)

    def handle_event(self, event):
        if event.x > 750 - 25 and event.x < 750 + 25 and event.y > 755 - 25 and event.y < 755 + 25:
            self.goto_pause();

    @staticmethod
    def goto_pause():
        game_framework.push_state(pause_state)