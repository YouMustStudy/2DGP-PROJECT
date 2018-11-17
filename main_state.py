WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CENTER = (WINDOW_WIDTH /2, WINDOW_HEIGHT - 400)

#라이브러리 임포트
from pico2d import *
import game_framework
import game_world

#게임상태 임포트
import inf_state
import pause_state

#클래스 임포트
from Player import Player
from Dice import DiceButton
import Tile
from PauseButton import PauseButton
from UI import UI

name = "MainState"

MAP = None
PLAYER = []
DICE = None
PHASE = None
PLAYER_TURN = None
PAUSE_BUTTON = None

CLICKED_TILE = 0 #팝업창을 띄울 타일

bgimage = None

def enter():
    global MAP, PLAYER, PLAYER_TURN, DICE, bgimage, PAUSE_BUTTON
    PLAYER_TURN = 0
    MAP = Tile.init_tile()
    PLAYER.append(Player(MAP[3].x, MAP[3].y, 'p'))
    DICE = DiceButton()
    PAUSE_BUTTON = PauseButton()
    bgimage = load_image('bgimage.jpg')


    P1UI = UI(120, 32, 0)
    P2UI = UI(WINDOW_WIDTH - 120, 32, 1)

    for tiles in MAP:
        game_world.add_object(tiles, 0)
    for character in PLAYER:
        game_world.add_object(character, 0)
    game_world.add_object(P1UI, 0)
    game_world.add_object(P2UI, 0)

    game_world.add_object(DICE, 1)
    game_world.add_object(PAUSE_BUTTON, 1)

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
            PAUSE_BUTTON.handle_event(event)
        else:
            pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    #bgimage.draw(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, WINDOW_WIDTH, WINDOW_HEIGHT)
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
            if tile.name == '찬스카드':
                break;
            game_framework.push_state(inf_state)