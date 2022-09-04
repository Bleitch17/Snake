import pygame

from enum import Enum


class Tile:
    class TileColors(Enum):
        BLACK = 0
        GREEN = 1

    COLOR_IMAGE_MAP = {
        TileColors.BLACK: './resources/Black_Tile.png',
        TileColors.GREEN: './resources/Green_Tile.png'
    }

    TILE_WIDTH = 20

    def __init__(self, tile_color, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

        self._tile = pygame.transform.scale(pygame.image.load(Tile.COLOR_IMAGE_MAP[tile_color]),
                                            (Tile.TILE_WIDTH, Tile.TILE_WIDTH))

    @property
    def tile(self):
        return self._tile
