import pyxel

import constants
import play_state
import state
import utils


class TitleState(state.State):
    def __init__(self, params) -> None:
        super().__init__()

        self.stack = params["stack"]

    def enter(self):
        pass

    def exit(self):
        self.stack.push(
            play_state.PlayState(
                {
                    "stack": self.stack,
                }
            )
        )

    def handle_input(self, inputs):
        if inputs.tapped("button_start"):
            self.stack.pop()

    def update(self):
        pass

    def draw(self):
        # Background
        pyxel.blt(
            0,
            0,
            constants.IDX_IMAGE_GUI,
            0,
            0,
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
        )

        # Title
        title = "Milky Way"
        utils.text(constants.SCREEN_WIDTH / 2 - utils.text_width(title) / 2, 18, title)

        # Start
        start = "Press Start"
        utils.text(constants.SCREEN_WIDTH / 2 - utils.text_width(start) / 2, 88, start)
