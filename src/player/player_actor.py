import pyxel

import app
import actor
import state_machine
import idle_state
import run_state
import jump_state
import fall_state
import climb_state
import talk_state
import utils

RUN_SPEED = 1.05


class Player(actor.Actor):
    def __init__(self, world, props, x, y):
        super().__init__(world, props, x, y)

        self.velocity_y_tween = None
        self.run_speed = RUN_SPEED

        self.state_machine = state_machine.StateMachine()
        self.state_machine.states["idle"] = player.idle_state.Idle(
            self, self.state_machine, world
        )
        self.state_machine.states["run"] = player.run_state.Run(
            self, self.state_machine, world
        )
        self.state_machine.states["jump"] = player.jump_state.Jump(
            self, self.state_machine, world
        )
        self.state_machine.states["fall"] = player.fall_state.Fall(
            self, self.state_machine, world
        )
        self.state_machine.states["climb"] = player.climb_state.Climb(
            self, self.state_machine, world
        )
        self.state_machine.states["talk"] = player.talk_state.Talk(
            self, self.state_machine, world
        )

        self.state_machine.change("idle")

    def get_touching_climbable(self):
        x = self.sprite.position[0]
        y = self.sprite.position[1]

        x1 = int((x + self.hitbox.left) // 8)
        y1 = int((y + self.hitbox.top) // 8)
        x2 = int((x + self.hitbox.right - 1) // 8)
        y2 = int((y + self.hitbox.bottom - 1) // 8)

        for yi in range(y1, y2 + 1):
            for xi in range(x1, x2 + 1):
                if self.world.map.is_climbable(xi, yi):
                    return (xi, yi)

        return None

    def handle_input(self, inputs):
        self.state_machine.handle_input(inputs)

    def update(self):
        self.state_machine.update()

    def draw(self):
        super().draw()
        self.state_machine.draw()

        if app.g_debug:
            utils.text_label(0, 16, "{}".format(self.state_machine.current.name))

            utils.text_label(
                0,
                pyxel.FONT_HEIGHT,
                "{}".format(self.sprite.position),
            )
