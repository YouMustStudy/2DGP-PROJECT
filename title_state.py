import game_framework
import menu_state
from pico2d import *


name = "TitleState"
logo = None
bg = None
alpha = 0
status = 0

def enter():
    global logo, bg, alpha, status
    if logo == None:
        logo = load_image('.\\popup\\logo.png')
    if bg == None:
        bg = load_image('.\\popup\\titlebg.png')
    alpha = 0
    status = 0


def exit():
    global logo, bg
    del(logo)
    del(bg)


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()


def draw():
    bg.draw(400, 400)
    logo.draw(400, 400)






def update():
    global alpha, status, logo
    if status == 0:
        alpha += game_framework.frame_time
        alpha = clamp(0, alpha, 1)
        logo.opacify(alpha)
        if alpha == 1:
            status = 1
    elif status == 1:
        alpha -= game_framework.frame_time
        alpha = clamp(0, alpha, 1)
        logo.opacify(alpha)
        if alpha == 0:
            game_framework.change_state(menu_state)



def pause():
    pass


def resume():
    pass