import pyxel


def text(x, y, text_str, col=7, shadow=1):
    pyxel.text(x, y + 1, text_str, shadow)
    pyxel.text(x, y, text_str, col)


def text_width(text_str):
    return len(text_str) * pyxel.FONT_WIDTH
