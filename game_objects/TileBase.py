import pygame

from enum import Enum


class TileBase:
    class TileColors(Enum):
        BLACK = 0
        GREEN = 1
        RED = 2

    COLOR_IMAGE_MAP = {
        TileColors.BLACK: './resources/Black_Tile.png',
        TileColors.GREEN: './resources/Green_Tile.png',
        TileColors.RED:   './resources/apple.png'
    }

    TILE_WIDTH = 20

    def __init__(self, tile_color):
        self._tile = pygame.transform.scale(pygame.image.load(TileBase.COLOR_IMAGE_MAP[tile_color]),
                                            (TileBase.TILE_WIDTH, TileBase.TILE_WIDTH))
