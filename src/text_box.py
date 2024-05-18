
import pyxel

import state
import utils
import constants
import rect
import panel

class TextBox(state.State):
    def __init__(self, params) -> None:
        super().__init__()

        self.stack = params["stack"]

        self.box_size = params.get("box_size", (constants.SCREEN_W,40))
        self.padding = params.get("padding", 8)
        self.text_colour = params.get("text_col", 7)

        self.on_finish = params.get("on_finish")

        self.panel = panel.Panel(params.get("panel_params"))
        self.panel.set_position(
            0,
            constants.SCREEN_H-self.box_size[1],
            self.box_size[0]//4,
            self.box_size[1]//4
        )

        x = self.panel.get_position()[0] + self.padding
        y = self.panel.get_position()[1] + self.padding
        self.text_area = rect.Rect(
            x,
            y,
            self.box_size[0] - self.padding * 2,
            self.box_size[1] - self.padding * 2,
        )

        text_w = self.text_area.w // pyxel.FONT_WIDTH
        text_h = self.text_area.h // pyxel.FONT_HEIGHT
        self.chunks = utils.text_box_chunks(
            params["text"],
            text_h,
            text_w
        )
        self.chunk_index = 0

        #print(self.chunks)

    def enter(self, enter_params=None):
        pass

    def exit(self):
        if self.on_finish:
            self.on_finish()

    def handle_input(self, inputs):
        if inputs.tapped("button_attack"):
            if self.chunk_index < len(self.chunks) - 1:
                self.chunk_index += 1
            else:
                self.stack.pop()

    def update(self):
        pass

    def draw(self):
        self.panel.draw()

        line_y = 0
        for line in self.chunks[self.chunk_index]:
            utils.text(
                self.text_area.x, 
                self.text_area.y + line_y, 
                line,
                self.text_colour
            )
            line_y += pyxel.FONT_HEIGHT

        utils.text_label(
            self.text_area.right 
                + self.padding
                - pyxel.FONT_WIDTH*3,
            self.text_area.bottom 
                + self.padding
                - pyxel.FONT_HEIGHT,
            "v",
        )
