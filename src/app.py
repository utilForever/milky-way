import pyxel

import constants
import state_stack
import input

g_debug = False


class App:
    def __init__(self):
        pyxel.init(
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
            constants.TITLE,
            constants.FPS,
            display_scale=3,
            capture_scale=1,
            capture_sec=20,
        )

        self.input = input.Input()

        self.stack = state_stack.StateStack()

        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_F1):
            global g_debug
            g_debug = not g_debug

        self.stack.update(self.input)

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        self.stack.draw()


App()
