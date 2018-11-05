import random
import json
import os

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

import inf_state
import pause_state

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


CLICKED_TILE = 0 #팝업창을 띄울 타일

bgimage = None
menu = None

def enter():
    global MAP, PLAYER, PLAYER_TURN, DICE, bgimage, menu
    PLAYER_TURN = 0
    MAP = TileClass.init_tile()
    PLAYER.append(PlayerClass.Player(MAP[3].x, MAP[3].y, 'p'))
    DICE = DiceClass.Dice()
    bgimage = load_image('bgimage.jpg')
    menu = load_image('.\\icons\\settings.png')

    #game_world.add_object(MAP, 0)
    for tiles in MAP:
        game_world.add_object(tiles, 0)
    for character in PLAYER:
        game_world.add_object(character, 0)
    game_world.add_object(DICE, 1)

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
            event.y = WINDOW_HEIGHT - event.y + 1
            DICE.handle_event(event)
            popup_event(event)
            if event.x > 750-25 and event.x < 750+25 and event.y > 750-25 and event.y < 750+25:
                game_framework.push_state(pause_state)
        else:
            pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    bgimage.draw(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT)
    menu.draw(750, 750, 50, 50)
    for game_object in game_world.all_objects():
        game_object.draw()


def rotate_map(theta):
    for tiles in MAP:
        tiles.rotate(theta)

def fix_map():
    for tiles in MAP:
        tiles.fix_position()

def popup_event(event):
    global CLICKED_TILE
    for tile in MAP:
        if tile.isclicked(event.x, event.y) == 1:
            CLICKED_TILE = tile
            game_framework.push_state(inf_state)