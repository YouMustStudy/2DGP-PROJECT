from pico2d import *
import game_framework
import main_state

image = None
playbutton = (395, 320)
exitbutton = (395, 180)
button_width = 140
button_height = 50

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
        event.y = 800 - event.y + 1
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.x > playbutton[0] - button_width and event.x < playbutton[0] + button_width and event.y > playbutton[1] - button_height and event.y < playbutton[1] + button_height:
                game_framework.change_state(main_state)
            elif event.x > exitbutton[0] - button_width and event.x < exitbutton[0] + button_width and event.y > exitbutton[1] - button_height and event.y < exitbutton[1] + button_height:
                game_framework.quit()
        else:pass

def pause(): pass
def resume(): pass