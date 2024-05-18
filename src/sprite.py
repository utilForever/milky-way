import pyxel

import constants


class Sprite:
    def __init__(self, props, x, y):
        self.position = [x, y]
        self.animations = props.get("states", None)
        self.image_bank = constants.IDX_IMAGE_SPRITES
        self.color_key = props.get("color_key", pyxel.COLOR_BLACK)
        self.state = props.get("start_state", "idle")

        if len(self.animations) == 1:
            self.state = next(iter(self.animations))

        self.frame = props.get("start_frame", 0)
        self.frame_time = 0
        self.flip_horizontal = props.get("flip_horizontal", False)
        self.flip_vertical = props.get("flip_vertical", False)
        self.size = props.get("size", (8, 8))
        self.visible = props.get("visible", True)
        self.animation_finished = False
        self.animation_paused = False

    def set_state(self, state):
        if state not in self.animations:
            return

        if state == self.state:
            return

        self.state = state
        self.frame = 0
        self.frame_time = 0
        self.animation_finished = False

    def get_frame_uv(self):
        return self.animations[self.state]["frames"][self.frame]

    def animate(self):
        if self.animation_paused:
            return

        if self.animations:
            self.frame_time += constants.SECS_PER_FRAME

            if self.frame_time >= self.animations[self.state]["frame_speed"]:
                self.frame_time = 0
                self.frame += 1

                if self.frame == len(self.animations[self.state]["frames"]):
                    loop = self.animations[self.state].get("loop")

                    if loop is not None:
                        if loop:
                            self.frame = 0
                        else:
                            self.frame -= 1
                            self.animation_finished = True
                    else:
                        self.frame = 0

    def update(self):
        self.animate()

    def draw(self, camera=None):
        if not self.visible:
            return

        uv = self.get_frame_uv()

        pyxel.blt(
            pyxel.floor(self.position[0] - camera.rect.left),
            pyxel.floor(self.position[1] - camera.rect.top),
            self.image_bank,
            uv[0],
            uv[1],
            -self.size[0] if self.flip_horizontal else self.size[0],
            -self.size[1] if self.flip_vertical else self.size[1],
            self.color_key,
        )
