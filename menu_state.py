from pico2d import *
import game_framework
import main_state

menu = None
select = None
bgm = None
playbutton = (395, 320)
exitbutton = (395, 180)
mode = 0
button_width = 140
button_height = 50

def enter():
    global menu, bgm, mode, select
    mode = 0
    menu = load_image('.\\popup\\menu.png')
    select = load_image('.\\popup\\select.png')
    bgm = load_music('.\\sound\\GameWaitting_Original.mp3')
    bgm.repeat_play()

def exit():
    global bgm, menu, select
    del(select)
    del(menu)
    del(bgm)

def update(): pass
def draw():
    if mode == 0:
        menu.draw(400, 400)
    else:
        select.draw(400, 400)


def handle_events():
    global mode
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            if mode == 0:
                game_framework.quit()
            else:
                mode = 1
        elif event.type == SDL_MOUSEBUTTONDOWN:
            event.y = 800 - event.y + 1
            if event.x > playbutton[0] - button_width and event.x < playbutton[0] + button_width and event.y > playbutton[1] - button_height and event.y < playbutton[1] + button_height:
                if mode == 0:
                    mode = 1
                else:
                    main_state.set_mode(0)
                    game_framework.change_state(main_state)
            elif event.x > exitbutton[0] - button_width and event.x < exitbutton[0] + button_width and event.y > exitbutton[1] - button_height and event.y < exitbutton[1] + button_height:
                if mode == 0:
                    game_framework.quit()
                else:
                    main_state.set_mode(1)
                    game_framework.change_state(main_state)
        else:pass

def pause(): pass
def resume(): pass