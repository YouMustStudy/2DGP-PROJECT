import game_framework
import pico2d

import main_state

import title_state

pico2d.open_canvas(main_state.WINDOW_WIDTH, main_state.WINDOW_HEIGHT)
game_framework.run(title_state)
pico2d.close_canvas()