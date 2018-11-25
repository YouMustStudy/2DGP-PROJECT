from pico2d import *
import main_state
import game_framework

image = None
width = None
height = None
cur_state = None


def enter():
    global image, width, height, cur_state
    if image == None:
        image = load_image('.\\popup\\pause.png')
    width = height = 0
    cur_state = EnterState

def exit():
    pass

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_state()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            event.y=main_state.WINDOW_HEIGHT - event.y + 1
            cur_state.handle_events(event)
            if event.x > 750 - 25 and event.x < 750 + 25 and event.y > 755 - 25 and event.y < 755 + 25:
                game_framework.pop_state()


def update():
    cur_state.update()


def draw():
    game_framework.stack[0].draw()
    cur_state.draw()

class EnterState:
    @staticmethod
    def draw():
        image.draw(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2, width, height)

    @staticmethod
    def update():
        global width, height, image
        width += image.w * game_framework.frame_time *15
        height += image.h * game_framework.frame_time *15
        width = clamp(0, width, image.w)
        height = clamp(0, height, image.h)
        if width == image.w:
            global cur_state
            cur_state = IdleState

    @staticmethod
    def handle_events(event):
        pass


class IdleState:
    @staticmethod
    def draw():
        image.draw(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2)

    @staticmethod
    def update():
        pass

    @staticmethod
    def handle_events(event):
        #RESUME
        if event.x > main_state.WINDOW_WIDTH/2 -67 and event.x < main_state.WINDOW_WIDTH/2 +67 and event.y > main_state.WINDOW_HEIGHT/2 +30-16 and event.y < main_state.WINDOW_HEIGHT/2 +30+ 16:
            global cur_state
            cur_state = ExitState
        #EXIT
        if event.x > main_state.WINDOW_WIDTH/2 -67 and event.x < main_state.WINDOW_WIDTH/2 +67 and event.y > main_state.WINDOW_HEIGHT/2 -15-16 and event.y < main_state.WINDOW_HEIGHT/2 -15+ 16:
            game_framework.quit()

class ExitState:
    @staticmethod
    def draw():
        image.draw(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2, width, height)

    @staticmethod
    def update():
        global width, height, image
        width -= image.w * game_framework.frame_time *15
        height -= image.h * game_framework.frame_time *15
        width = clamp(0, width, image.w)
        height = clamp(0, height, image.h)
        if width == 0:
            game_framework.pop_state()

    @staticmethod
    def handle_events(event):
        pass