import random
import json
import os

from pico2d import *
import game_framework
import game_world
import PlayerClass
import TileClass
import DiceClass

name = "MainState"

MAP = None
PLAYER = []
DICE = None
PHASE = None
PLAYER_TURN = None
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

test = None

def enter():
    global MAP, PLAYER, PLAYER_TURN, DICE, test
    test = load_image('Popup.png')
    PLAYER_TURN = 0
    MAP = TileClass.init_tile()
    PLAYER.append(PlayerClass.Player(MAP[0].x, MAP[0].y, 'p'))
    DICE = DiceClass.Dice()

    game_world.objects.insert(0, MAP)
    game_world.objects.insert(1, PLAYER)
    game_world.add_object(DICE, 2)

def exit():
    game_world.clear()


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
            DICE.handle_event(event)
        else:
            pass
            #boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    test.draw(WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
    update_canvas()


def rotate_map(theta):
    for tiles in MAP:
        tiles.rotate(theta)

def fix_map():
    for tiles in MAP:
        tiles.fix_position()