from pico2d import *
import game_framework
import main_state
import math
import game_world
import random

from Tile import Bigtile

Title = None
mag = None
sound = None
player = None

def enter():
    global Title, sound, player
    player = main_state.PLAYER[main_state.PLAYER_TURN]
    if Title == None:
        Title = load_image(".\\icons\\dest1.png")
    if sound == None:
        sound = load_wav('.\\sound\\ChanceCardWantCity_A01.wav')
    sound.play()
    if player.AI:
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
    global mag
    for tile in main_state.MAP:
        if type(tile) != Bigtile and tile.name != '찬스카드' and tile.isclicked(event.x, event.y) == 1:
            if mag == None:
                mag = Mag(tile)
            else:
                mag.set_tile(tile)
            main_state.change_turn()
            game_framework.pop_state()

def AI_set_dst():
    global mag
    index = random.randint(0, 27)
    if index % 7 == 0:
        index+=1
    if main_state.MAP[index].name == '찬스카드':
        index+=1

    tile = main_state.MAP[index]
    if mag == None:
        mag = Mag(tile)
    else:
        mag.set_tile(tile)
    main_state.change_turn()
    game_framework.pop_state()


class Mag:
    image = None
    def __init__(self, tile):
        if Mag.image == None:
            Mag.image = load_image(".\\icons\\X2.png")
        self.tile = tile
        self.tile.mag = 2
        game_world.add_object(self, 0)

    def update(self):
        pass

    def draw(self):
        self.image.rotate_draw(math.radians(self.tile.theta), self.tile.x, self.tile.y)

    def set_tile(self, tile):
        self.tile.mag = 1
        self.tile = tile
        self.tile.mag = 2