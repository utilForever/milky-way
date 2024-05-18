import pyxel


class Rect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.w}, {self.h})"

    @property
    def left(self):
        return self.x

    @property
    def right(self):
        return self.x + self.w

    @property
    def top(self):
        return self.y

    @property
    def bottom(self):
        return self.y + self.h

    @property
    def mid_x(self):
        return self.x + (self.w / 2)

    @property
    def mid_y(self):
        return self.y + (self.h / 2)

    def is_overlapping(self, x, y, w, h):
        return all((self.x < x + w, self.right > x, self.y < y + h, self.bottom > y))

    def is_overlapping_other(self, other):
        return all(
            (
                self.x < other.right,
                self.right > other.x,
                self.y < other.bottom,
                self.bottom > other.y,
            )
        )

    def draw(self, col):
        pyxel.rect(self.x, self.y, self.w, self.h, col)
