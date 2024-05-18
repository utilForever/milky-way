
import pyxel

import state
import utils
import constants
import rect
import panel

class ChoiceBox(state.State):
    def __init__(self, params) -> None:
        super().__init__()

        self.stack = params["stack"]

        self.box_size = params.get("box_size", (constants.SCREEN_W,40))
        self.padding = params.get("padding", 8)
        self.text_colour = params.get("text_col", 7)
        self.show_caret = False

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

        self.choices = params.get("choices", [])
        self.selected_choice = 0

    def enter(self, enter_params=None):
        pass

    def exit(self):
        if self.on_finish:
            self.on_finish(self.selected_choice)

    def handle_input(self, inputs):
        if inputs.tapped("up"):
            self.selected_choice = (self.selected_choice - 1) % len(self.choices)
        elif inputs.tapped("down"):
            self.selected_choice = (self.selected_choice + 1) % len(self.choices)
        elif inputs.tapped("button_start"):
            self.stack.pop()

    def update(self):
        pass
    
    def draw(self):
        self.panel.draw()

        line_y = 0
        for i, choice in enumerate(self.choices):
            if i == self.selected_choice:
                choice_text = "> " + choice
            else:
                choice_text = "  " + choice
            utils.text(
                self.text_area.x,
                self.text_area.y + line_y,
                choice_text,
                self.text_colour,
            )
            line_y += pyxel.FONT_HEIGHT