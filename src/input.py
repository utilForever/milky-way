import pyxel

CONFIG = {
    "up": pyxel.KEY_W,
    "down": pyxel.KEY_S,
    "left": pyxel.KEY_A,
    "right": pyxel.KEY_D,
    "button_talk": pyxel.KEY_Q,
    "button_jump": pyxel.KEY_SPACE,
    "button_start": pyxel.KEY_RETURN,
}


class Input:
    def __init__(self) -> None:
        self._tapped = {}
        self._pressing = {}

    def tapped(self, key_name):
        return self._tapped.get(key_name)

    def pressing(self, key_name):
        return self._pressing.get(key_name)

    def update(self):
        for key in CONFIG.keys():
            self._tapped[key] = pyxel.btn(CONFIG[key])
            self._pressing[key] = pyxel.btn(CONFIG[key])
