WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
CENTER = (WINDOW_WIDTH /2, WINDOW_HEIGHT - 400)

#라이브러리 임포트
from pico2d import *
import game_framework
import game_world

#게임상태 임포트
import inf_state

#클래스 임포트
from Player import Player, SpinState
from Dice import DiceButton
import Tile
from PauseButton import PauseButton
from UI import UI

name = "MainState"

MAP = None
PLAYER = []
BUILDING = []
DICE = None
PHASE = None
PLAYER_TURN = None
PAUSE_BUTTON = None


#턴 넘김시 시작했음을 알리는 플래그
START_FLAG = False

CLICKED_TILE = 0 #팝업창을 띄울 타일

bgimage = None
bgm = None

def enter():
    global MAP, PLAYER, PLAYER_TURN, DICE, PAUSE_BUTTON, BUILDING, bgm
    PLAYER_TURN = 0
    MAP = Tile.init_tile()
    PLAYER.append(Player(0, MAP[0].x, MAP[0].y, 'g', 0))
    PLAYER.append(Player(1, MAP[0].x, MAP[0].y, 'b', 1))
    DICE = DiceButton()
    PAUSE_BUTTON = PauseButton()

    P1UI = UI(150, 40, 0, PLAYER[0])
    P2UI = UI(WINDOW_WIDTH - 150, 40, 1, PLAYER[1])

    for tiles in MAP:
        game_world.add_object(tiles, 0)
    for character in PLAYER:
        game_world.add_object(character, 1)
    game_world.add_object(P1UI, 0)
    game_world.add_object(P2UI, 0)

    game_world.add_object(DICE, 1)
    game_world.add_object(PAUSE_BUTTON, 1)

    bgm = load_music('.\\sound\\GamePlay1.mp3')
    bgm.repeat_play()



def exit():
    global bgm
    game_world.clear()
    MAP.clear()
    PLAYER.clear()
    BUILDING.clear()
    del(bgm)



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
            PAUSE_BUTTON.goto_pause()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            event.y = WINDOW_HEIGHT - event.y + 1
            DICE.handle_event(event)
            popup_event(event)
            PAUSE_BUTTON.handle_event(event)
        else:
            cheat_move(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    for game_object in game_world.all_objects():
        game_object.draw()


def rotate_map(theta):
    for tiles in MAP:
        tiles.rotate(theta)

def rotate_player(theta):
    for player in PLAYER:
        player.rotate(theta)

def rotate_building(theta):
    for building in BUILDING:
        building.rotate(theta)

def rotate_world(theta):
    rotate_player(-theta)
    rotate_building(-theta)
    rotate_map(-theta)

def fix_map():
    for tiles in MAP:
        tiles.fix_position()

def popup_event(event):
    global CLICKED_TILE
    for tile in MAP:
        if type(tile) != Tile.Bigtile and tile.isclicked(event.x, event.y) == 1:
            CLICKED_TILE = tile
            if tile.name == '찬스카드':
                break;
            game_framework.push_state(inf_state)

def check_rank():
    if PLAYER[0].money == PLAYER[1].money:
        PLAYER[0].rank = 1
        PLAYER[1].rank = 1
    elif PLAYER[0].money > PLAYER[1].money:
        PLAYER[0].rank = 1
        PLAYER[1].rank = 2
    elif PLAYER[0].money < PLAYER[1].money:
        PLAYER[0].rank = 2
        PLAYER[1].rank = 1

def change_turn():
    global PLAYER_TURN, START_FLAG

    PLAYER[PLAYER_TURN].image.opacify(0.6)
    PLAYER_TURN = (PLAYER_TURN+1) % 2
    PLAYER[PLAYER_TURN].image.opacify(1.0)

    if PLAYER[PLAYER_TURN].event == 1:
        PLAYER[PLAYER_TURN].event = 0
        change_turn()
        return

    START_FLAG = True
    PLAYER[PLAYER_TURN].change_state(SpinState)

def trade_money():
    index = PLAYER[PLAYER_TURN].index
    owner = MAP[index].owner
    cost = MAP[index].return_cost()

    PLAYER[PLAYER_TURN].cash -= cost
    PLAYER[PLAYER_TURN].money -= cost
    PLAYER[owner].cash += cost
    PLAYER[owner].money += cost

def cheat_move(event):
    if event.type == SDL_KEYDOWN:
        if event.key >= 49 and event.key <= 54:
            PLAYER[PLAYER_TURN].move = event.key-48
            DICE.visible=1