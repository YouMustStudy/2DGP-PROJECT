from pico2d import *
from Building import Building
import game_framework
import game_world
import main_state

image = None
width = None
height = None
cur_state = None

clicked_tile = None #클릭된 타일
CUR_TURN = 0 #현재 턴
lens = None #출력 될 글자 수
check = None #V자 아이콘
cross = None #X자 아이콘
purchase = None #건설 아이콘

min_level = None #필수적으로 건설해야하는 레벨
select_level = None #현재 선택된 건설레벨
max_level = None #건설가능한 최대 레벨
total_cost = None #총 건설비

EndTimer = 0.0
EndFlag = False

#아이콘 위치
pos = [(158, 408),
       (292, 408),
       (427, 408),
       (562, 408)]

#팝업창에 사용될 폰트들
title_font = None
money_font = None
passing_font = None
cost_font = None

def enter():
    global image, width, height, cur_state, title_font, money_font, clicked_tile, lens, check, cross, min_level, max_level, select_level, total_cost, purchase, passing_font, cost_font, CUR_TURN, EndFlag, EndTimer
    if image == None:
        image = load_image('.\\popup\\upgrade.png')
    if title_font == None:
        title_font = load_font('.\\font\\InterparkGothicBold.ttf', 40)
    if money_font == None:
        money_font = load_font('.\\font\\InterparkGothicBold.ttf', 18)
    if passing_font == None:
        passing_font = load_font('.\\font\\InterparkGothicBold.ttf', 24)
    if cost_font == None:
        cost_font = load_font('.\\font\\InterparkGothicBold.ttf', 30)
    if purchase == None:
        purchase = PurchaseIcon(main_state.WINDOW_WIDTH/2 + 16, main_state.WINDOW_HEIGHT/2 - 97)
    width = height = 0
    EndTimer = 0.3
    EndFlag = False
    CUR_TURN = main_state.PLAYER_TURN


    clicked_tile = main_state.MAP[main_state.PLAYER[CUR_TURN].index]
    min_level = clicked_tile.level+1
    select_level = min_level
    max_level = min(main_state.PLAYER[CUR_TURN].round, 3)

    total_cost = clicked_tile.BuildingCost[min_level]

    check = [CheckIcon(pos[i]) for i in range(max_level + 1)]
    cross = [CrossIcon(pos[i]) for i in range(max_level+1, 4)]

    for i in range(0, min_level +1):
        check[i].visible = 1

    lens = [len(clicked_tile.name),
           len(str(clicked_tile.BuildingCost[0])),
           len(str(clicked_tile.BuildingCost[1])),
           len(str(clicked_tile.BuildingCost[2])),
           len(str(clicked_tile.BuildingCost[3])),
           len(str(clicked_tile.PassingCost[min_level])),
           len(str(total_cost))
            ]

    cur_state = EnterState


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
            cur_state.handle_events(event)
            main_state.PAUSE_BUTTON.handle_event(event)
        else:
            pass


def update():
    game_framework.stack[0].update()
    cur_state.update()


def draw():
    game_framework.stack[0].draw()
    cur_state.draw()

class EnterState:
    @staticmethod
    def draw():
        image.draw(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2, width, height)

    @staticmethod
    def update():
        global width, height, image
        width += image.w * game_framework.frame_time *15
        height += image.h * game_framework.frame_time *15
        width = clamp(0, width, image.w)
        height = clamp(0, height, image.h)
        if width == image.w:
            global cur_state
            cur_state = IdleState

    @staticmethod
    def handle_events(event):
        pass


class IdleState:
    @staticmethod
    def draw():
        image.draw(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2)
        purchase.draw()

        #도시이름 출력
        title_font.draw(main_state.WINDOW_WIDTH/2 - 20*lens[0], main_state.WINDOW_HEIGHT/2 + 145, clicked_tile.name,(223, 233, 236))
        #건설비용 출력
        money_font.draw(main_state.WINDOW_WIDTH / 2 - 180 - 6*lens[1], main_state.WINDOW_HEIGHT / 2 - 22, str(clicked_tile.BuildingCost[0]) + '만', (198, 54, 23))
        money_font.draw(main_state.WINDOW_WIDTH / 2 - 45 - 6*lens[2], main_state.WINDOW_HEIGHT / 2 - 22, str(clicked_tile.BuildingCost[1]) + '만', (198, 54, 23))
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 90 - 6*lens[3], main_state.WINDOW_HEIGHT / 2 - 22, str(clicked_tile.BuildingCost[2]) + '만', (198, 54, 23))
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 225 - 6*lens[4], main_state.WINDOW_HEIGHT / 2 - 22, str(clicked_tile.BuildingCost[3]) + '만', (198, 54, 23))
        #통행료 출력
        passing_font.draw(main_state.WINDOW_WIDTH / 2 + 50 - 6*lens[5], main_state.WINDOW_HEIGHT / 2 - 153, str(clicked_tile.PassingCost[select_level]) + '만', (94, 85, 70))
        #총 건설비용 출력
        cost_font.draw(main_state.WINDOW_WIDTH / 2 + 34 - 6 * lens[6], main_state.WINDOW_HEIGHT / 2 - 97, str(total_cost) + '만', (146, 49, 33))

        #종료버튼 BB
        #r = 27
        #x = 663
        #y = 598
        #draw_rectangle(x-r, y-r, x+r, y+r)

        for icon in check:
            icon.draw()
        for icon in cross:
            icon.draw()


    @staticmethod
    def update():
        pass

    @staticmethod
    def handle_events(event):
        #구매버튼 클릭시
        if(purchase.handle_events(event)):
            global total_cost, select_level, cur_state, EndFlag
            main_state.PLAYER[CUR_TURN].cash -= total_cost #건설비용 지불
            clicked_tile.owner = CUR_TURN #소유권 변경

            for i in range(clicked_tile.level+1, select_level + 1): #건물 객체 추가
                building = Building(i, CUR_TURN, clicked_tile)
                game_world.add_object(building, 1)
                main_state.BUILDING.append(building)

            clicked_tile.level = select_level #건설레벨 적용
            EndFlag = True
            cur_state = ExitState
        for i in range(min_level, max_level+1):
            if(check[i].handle_events(event) == 1):
                global lens
                total_cost = 0
                select_level = i
                #체크 아이콘 재설정
                for j in range(min_level, i+1):
                    check[j].visible = 1
                    total_cost+=clicked_tile.BuildingCost[j] #건설비용 재산정
                for j in range(i+1, max_level+1):
                    check[j].visible = 0

                lens[5] = len(str(clicked_tile.PassingCost[select_level]))
                lens[6] = len(str(total_cost))
                if total_cost > main_state.PLAYER[CUR_TURN].cash:
                    purchase.visible = 0
                else:
                    purchase.visible = 1

        #종료버튼
        if event.x > 663 - 27 and event.x < 663 + 27 and event.y > 548 - 27 and event.y < 548 + 27:
            cur_state = ExitState

class ExitState:
    @staticmethod
    def draw():
        image.draw(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2, width, height)

    @staticmethod
    def update():
        global width, height, image
        width -= image.w * game_framework.frame_time *15
        height -= image.h * game_framework.frame_time *15
        width = clamp(0, width, image.w)
        height = clamp(0, height, image.h)
        if width == 0:
            if EndFlag:
                global EndTimer
                EndTimer -= game_framework.frame_time
                if EndTimer <= 0:
                    game_framework.pop_state()
                    main_state.change_turn()
            else:
                game_framework.pop_state()
                main_state.change_turn()

    @staticmethod
    def handle_events(event):
        pass

class CrossIcon:
    image = None
    def __init__(self, pos):
        self.x, self.y = pos[0], pos[1]
        if CrossIcon.image == None:
            CrossIcon.image = load_image('.\\icons\\cross.png')

    def draw(self):
        self.image.draw(self.x, self.y, 32, 27)


class CheckIcon:
    image = None
    def __init__(self, pos):
        self.x, self.y = pos[0], pos[1]
        self.visible = 0
        if CheckIcon.image == None:
            CheckIcon.image = load_image('.\\icons\\check.png')

    def draw(self):
        self.image.clip_draw(32 * self.visible, 0, 32, 27, self.x, self.y, 32, 27)

    def handle_events(self, event):
        if event.x > self.x - 16 and event.x < self.x + 16 and event.y > self.y-13 and event.y < self.y+13:
            return 1
        return 0

class PurchaseIcon:
    image = None
    def __init__(self, x, y):
        self.x , self.y = x, y
        self.visible = 1
        if PurchaseIcon.image == None:
            PurchaseIcon.image = load_image('.\\icons\\purchase.png')

    def draw(self):
        #구매버튼 BB
        #draw_rectangle(self.x-165, self.y-33, self.x+165, self.y+33)
        self.image.clip_draw(330 * self.visible, 0, 330, 66, self.x, self.y)

    def handle_events(self, event):
        if self.visible and event.x > self.x - 165 and self.x + 165 and event.y > self.y-33 and event.y < self.y+33:
            return 1
        return 0