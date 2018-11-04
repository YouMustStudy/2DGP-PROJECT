from pico2d import *
import game_framework
import main_state

image = None
width = None
height = None
cur_state = None

clicked_tile = None #클릭된 타일
lens = None #출력 될 글자 수
check = None #V자 아이콘
cross = None #X자 아이콘
purchase = None #건설 아이콘

min_level = None #필수적으로 건설해야하는 레벨
select_level = None #현재 선택된 건설레벨
max_level = None #건설가능한 최대 레벨
total_cost = None #총 건설비

#아이콘 위치
pos = [(main_state.WINDOW_WIDTH/2 + 66, main_state.WINDOW_HEIGHT/2 + 30),
       (main_state.WINDOW_WIDTH / 2 + 66, main_state.WINDOW_HEIGHT / 2 + 13),
       (main_state.WINDOW_WIDTH / 2 + 66, main_state.WINDOW_HEIGHT / 2 - 4),
       (main_state.WINDOW_WIDTH / 2 + 66, main_state.WINDOW_HEIGHT / 2 - 20)]

#팝업창에 사용될 폰트들
title_font = None
money_font = None

def enter():
    global image, width, height, cur_state, title_font, money_font, clicked_tile, lens, check, cross, min_level, max_level, select_level, total_cost, purchase
    if image == None:
        image = load_image('.\\popup\\upgrade.png')
    if title_font == None:
        title_font = load_font('.\\font\\InterparkGothicBold.ttf', 20)
    if money_font == None:
        money_font = load_font('.\\font\\InterparkGothicBold.ttf', 10)
    if purchase == None:
        purchase = PurchaseIcon(main_state.WINDOW_WIDTH/2, main_state.WINDOW_HEIGHT/2 - 91)
    width = height = 0


    clicked_tile = main_state.MAP[main_state.PLAYER[main_state.PLAYER_TURN].index]
    min_level = clicked_tile.level+1
    select_level = min_level
    max_level = min(main_state.PLAYER[main_state.PLAYER_TURN].round, 3)

    total_cost = clicked_tile.BuildingCost[min_level]

    check = [CheckIcon(pos[i]) for i in range(max_level + 1)]
    cross = [CrossIcon(pos[i]) for i in range(max_level+1, 4)]

    for i in range(0, min_level +1):
        check[i].visible = 0

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
                game_framework.quit()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            event.y = main_state.WINDOW_HEIGHT - event.y + 1
            cur_state.handle_events(event)
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
        title_font.draw(main_state.WINDOW_WIDTH/2 - 10*lens[0], main_state.WINDOW_HEIGHT/2 + 88, clicked_tile.name,(255, 255, 255))
        #건설비용 출력
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 48 - 6*lens[1], main_state.WINDOW_HEIGHT / 2 + 30, str(clicked_tile.BuildingCost[0]) + '만')
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 48 - 6*lens[2], main_state.WINDOW_HEIGHT / 2 + 12, str(clicked_tile.BuildingCost[1]) + '만')
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 48 - 6*lens[3], main_state.WINDOW_HEIGHT / 2 - 5, str(clicked_tile.BuildingCost[2]) + '만')
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 48 - 6*lens[4], main_state.WINDOW_HEIGHT / 2 - 22, str(clicked_tile.BuildingCost[3]) + '만')
        #통행료 출력
        title_font.draw(main_state.WINDOW_WIDTH / 2 - 6*lens[5], main_state.WINDOW_HEIGHT / 2 - 63, str(clicked_tile.PassingCost[select_level]), (255, 0, 0))
        title_font.draw(main_state.WINDOW_WIDTH / 2 + 30, main_state.WINDOW_HEIGHT / 2 - 63, '만', (255, 0, 0))
        #총 건설비용 출력
        money_font.draw(main_state.WINDOW_WIDTH / 2 + 17 - 6 * lens[6], main_state.WINDOW_HEIGHT / 2 - 91, str(total_cost) + '만', (146, 49, 33))

        r = 17
        x = main_state.WINDOW_WIDTH/2 + 68
        y = main_state.WINDOW_HEIGHT/2 + 90
        draw_rectangle(x-r, y-r, x+r, y+r)

        for icon in check:
            icon.draw()
        for icon in cross:
            icon.draw()


    @staticmethod
    def update():
        pass

    @staticmethod
    def handle_events(event):
        if(purchase.handle_events(event)):
            global total_cost, select_level
            main_state.PLAYER[main_state.PLAYER_TURN].cash -= total_cost #건설비용 지불
            clicked_tile.owner = main_state.PLAYER_TURN #소유권 변경
            clicked_tile.level = select_level #건설레벨 적용
            game_framework.pop_state() #건설상태 종료
        for i in range(min_level, max_level+1):
            if(check[i].handle_events(event) == 1):
                global lens
                total_cost = 0
                select_level = i
                #체크 아이콘 재설정
                for j in range(min_level, i+1):
                    check[j].visible = 0
                    total_cost+=clicked_tile.BuildingCost[j] #건설비용 재산정
                for j in range(i+1, max_level+1):
                    check[j].visible = 1

                lens[5] = len(str(clicked_tile.PassingCost[select_level]))
                lens[6] = len(str(total_cost))
                if total_cost > main_state.PLAYER[main_state.PLAYER_TURN].cash:
                    purchase.visible = 1
                else:
                    purchase.visible = 0

        if event.x > main_state.WINDOW_WIDTH/2 + 51 and event.x < main_state.WINDOW_WIDTH/2 + 85 and event.y > main_state.WINDOW_HEIGHT/2 + 73 and event.y < main_state.WINDOW_HEIGHT/2 + 107:
            global cur_state
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
            game_framework.pop_state()

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
        self.image.draw(self.x, self.y)


class CheckIcon:
    image = None
    def __init__(self, pos):
        self.x, self.y = pos[0], pos[1]
        self.visible = 1
        if CheckIcon.image == None:
            CheckIcon.image = load_image('.\\icons\\check.png')

    def draw(self):
        self.image.clip_draw(10 * self.visible, 0, 10, 10, self.x, self.y)

    def handle_events(self, event):
        if event.x > self.x - 5 and self.x + 5 and event.y > self.y-5 and event.y < self.y+5:
            return 1
        return 0

class PurchaseIcon:
    image = None
    def __init__(self, x, y):
        self.x , self.y = x, y
        self.visible = 0
        if PurchaseIcon.image == None:
            PurchaseIcon.image = load_image('.\\icons\\purchase.png')

    def draw(self):
        self.image.clip_draw(123 * self.visible, 0, 123, 26, self.x, self.y)

    def handle_events(self, event):
        if self.visible == 0 and event.x > self.x - 60 and self.x + 60 and event.y > self.y-13 and event.y < self.y+13:
            return 1
        return 0