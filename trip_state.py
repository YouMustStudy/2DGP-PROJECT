from pico2d import *
import game_framework
import main_state
import random

Title = None
Player = None
sound = None
player = None

def enter():
    global Title, Player, sound
    if Title == None:
        Title = load_image(".\\icons\\dest.png")
    Player = main_state.PLAYER[main_state.PLAYER_TURN]
    if sound == None:
        sound = load_wav('.\\sound\\ChanceCardWantCity_A01.wav')
    sound.play()
    if Player.AI:
        AI_set_dst()

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
            set_dst(event)
            main_state.PAUSE_BUTTON.handle_event(event)
        else:
            pass

def update():
    game_framework.stack[0].update()


def draw():
    Title.draw(400, 300)
    game_framework.stack[0].draw()


def set_dst(event):
    global Player
    dst = 21
    for tile in main_state.MAP:
        if tile.isclicked(event.x, event.y) == 1:
            dst = main_state.MAP.index(tile)
            break

    if dst != 21:
        Player.move = dst - Player.index
        if Player.move < 0:
            Player.move = 28 + Player.move
        game_framework.pop_state()

def AI_set_dst():
    global Player
    dst = random.randint(0, 27)
    if dst == 21:
        dst += 1

    Player.move = dst - Player.index
    if Player.move < 0:
        Player.move = 28 + Player.move
    game_framework.pop_state()