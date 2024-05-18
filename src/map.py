import pyxel

import constants
import camera

SOLID_TILE_Y_MAX = 15
ONE_WAY_TILE_ROW = 15
CLIMBABLE_LIST = [
    (248 // 8, 248 // 8),
    (248 // 8, 240 // 8),
    (248 // 8, 232 // 8),
]


class Map:
    def __init__(self, params) -> None:
        self.world = params["world"]
        self.images = params.get("image", constants.IDX_IMAGE_TILES)
        self.tilemap = params["tilemap"]
        self.camera = camera.Camera()

    def is_climbable(self, tile_x, tile_y):
        tile = self.get_tile(tile_x, tile_y)
        return tile in CLIMBABLE_LIST

    def is_solid(self, tile_x, tile_y):
        tile = self.get_tile(tile_x, tile_y)
        return tile[1] < SOLID_TILE_Y_MAX

    def is_one_way(self, tile_x, tile_y):
        tile = self.get_tile(tile_x, tile_y)
        return tile[1] == ONE_WAY_TILE_ROW

    def get_tile(self, tile_x, tile_y):
        return pyxel.tilemap(self.tilemap).pget(tile_x, tile_y)

    def update(self):
        pass

    def draw(self):
        pyxel.bltm(
            0,
            0,
            self.images,
            self.camera.rect.left,
            self.camera.rect.top,
            self.camera.rect.width,
            self.camera.rect.height,
        )
