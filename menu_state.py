from pico2d import *
import game_framework

image = None

def enter():
    global image
    image = load_image('.\\popup\\menu.png')

def exit():
    global image
    del(image)

def update(): pass
def draw():
    image.draw(400, 400)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:pass
        else:pass

def pause(): pass
def resume(): pass