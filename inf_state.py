from pico2d import *
import game_framework
import main_state

image = None
width = None
height = None
name = '방콕'
len = len(name)
cur_state = None

title_font = None
money_font = None

def enter():
    global image, width, height, cur_state, title_font, money_font
    if image == None:
        image = load_image('Popup.png')
    if title_font == None:
        title_font = load_font('.\\font\\InterparkGothicBold.ttf', 20)
    if money_font == None:
        money_font = load_font('.\\font\\InterparkGothicBold.ttf', 10)
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
                game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            event.y = main_state.WINDOW_HEIGHT - event.y + 1
            cur_state.handle_events(event)
        else:
            pass


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
        title_font.draw(main_state.WINDOW_WIDTH/2 - 10*len, main_state.WINDOW_HEIGHT/2 + 88, name,(255, 255, 255))
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 58 - 12, main_state.WINDOW_HEIGHT / 2 + 30, '34' + '만')
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 58 - 18, main_state.WINDOW_HEIGHT / 2 + 12, '348' + '만')
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 58 - 18, main_state.WINDOW_HEIGHT / 2 - 5, '348' + '만')
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 58 - 18, main_state.WINDOW_HEIGHT / 2 - 22, '348' + '만')

        title_font.draw(main_state.WINDOW_WIDTH / 2 - 22, main_state.WINDOW_HEIGHT / 2 - 78, '2460', (255, 0, 0))
        title_font.draw(main_state.WINDOW_WIDTH / 2 + 30, main_state.WINDOW_HEIGHT / 2 - 78, '만', (255, 0, 0))
        r = 17
        x = main_state.WINDOW_WIDTH/2 + 68
        y = main_state.WINDOW_HEIGHT/2 + 90
        draw_rectangle(x-r, y-r, x+r, y+r)


    @staticmethod
    def update():
        pass

    @staticmethod
    def handle_events(event):
        if event.x > main_state.WINDOW_WIDTH/2 + 51 and event.x < main_state.WINDOW_WIDTH/2 + 85 and event.y > main_state.WINDOW_HEIGHT/2 + 73 and event.y < main_state.WINDOW_HEIGHT/2 + 107:
            global cur_state
            cur_state = ExitState

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