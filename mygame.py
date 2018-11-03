import game_framework
import pico2d

import main_state
import inf_state

pico2d.open_canvas(main_state.WINDOW_WIDTH, main_state.WINDOW_HEIGHT, sync=True)
game_framework.run(inf_state)
pico2d.close_canvas()