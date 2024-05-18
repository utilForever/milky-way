import constants
import rect


class Camera:
    def __init__(self):
        self.rect = rect.Rect(
            0,
            0,
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
        )

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y
