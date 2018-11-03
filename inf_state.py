from pico2d import *
import game_framework

image = None
width, height = 0

def enter():
    global image, width, height
    if image == None:
        image = load_image('Popup.png')
    width, height = 0

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

        else:
            pass


def update():
    pass


def draw():
    clear_canvas()

    update_canvas()