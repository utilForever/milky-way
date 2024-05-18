import pyxel

import constants
import state_stack
import input
import title_state

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

        self._load_resources()

        self.input = input.Input()

        self.stack = state_stack.StateStack()
        self.stack.push(
            title_state.TitleState(
                {
                    "stack": self.stack,
                    "inputs": self.input,
                }
            )
        )

        pyxel.run(self.update, self.draw)

    def _load_resources(self):
        pyxel.load("assets/res.pyxres")

        pyxel.image(constants.IDX_IMAGE_TILES).load(0, 0, constants.IMAGE_FILE_TILES)
        pyxel.image(constants.IDX_IMAGE_SPRITES).load(
            0, 0, constants.IMAGE_FILE_SPRITES
        )
        pyxel.image(constants.IDX_IMAGE_GUI).load(0, 0, constants.IMAGE_FILE_GUI)

    def update(self):
        if pyxel.btnp(pyxel.KEY_F1):
            global g_debug
            g_debug = not g_debug

        self.stack.update(self.input)

    def draw(self):
        pyxel.cls(pyxel.COLOR_BLACK)
        self.stack.draw()


App()
