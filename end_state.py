from pico2d import *
import game_framework
import main_state
import menu_state

image = None
width = None
height = None
cur_state = None

menubutton = (400, 345)
exitbutton = (400, 270)
button_width = 88
button_height = 23
selection = 0

IMAGE_EXPENTION_SPD = 15

def enter():
    global image, width, height, cur_state
    if image == None:
        image = load_image('.\\popup\\end.png')
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
                main_state.PAUSE_BUTTON.goto_pause()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            event.y = main_state.WINDOW_HEIGHT - event.y + 1
            cur_state.handle_events(event)
        else:
            pass


def update():
    #game_framework.stack[0].update()
    cur_state.update()


def draw():
    #game_framework.stack[0].draw()
    cur_state.draw()

class EnterState:
    @staticmethod
    def draw():
        image.draw(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2, width, height)


    @staticmethod
    def update():
        global width, height, image
        width += image.w * game_framework.frame_time * IMAGE_EXPENTION_SPD
        height += image.h * game_framework.frame_time * IMAGE_EXPENTION_SPD
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
        global cur_state, selection
        if event.x > menubutton[0] - button_width and event.x < menubutton[0] + button_width and event.y > menubutton[1] - button_height and event.y < menubutton[1] + button_height:
            selection = 0
            cur_state = ExitState
        elif event.x > exitbutton[0] - button_width and event.x < exitbutton[0] + button_width and event.y > exitbutton[1] - button_height and event.y < exitbutton[1] + button_height:
            selection = 1
            cur_state = ExitState



class ExitState:
    @staticmethod
    def draw():
        image.draw(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2, width, height)

    @staticmethod
    def update():
        global width, height, image, selection
        width -= image.w * game_framework.frame_time * IMAGE_EXPENTION_SPD
        height -= image.h * game_framework.frame_time * IMAGE_EXPENTION_SPD
        width = clamp(0, width, image.w)
        height = clamp(0, height, image.h)
        if width == 0:
            if selection == 0:
                pass
            if selection == 1:
                game_framework.quit();


    @staticmethod
    def handle_events(event):
        pass