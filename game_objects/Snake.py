from enum import Enum

from game_objects.Tile import Tile


class Snake:
    class Directions(Enum):
        RIGHT = 0
        LEFT = 1
        UP = 2
        DOWN = 3

    def __init__(self, x=0, y=0):
        self.x_pos = x
        self.y_pos = y

        self.length = 1

        self.head = Tile(Tile.TileColors.GREEN, x_pos=x, y_pos=y)

        self.x_vel = Tile.TILE_WIDTH
        self.y_vel = 0

        # TODO: list of tiles for the body, initially start at length 1

    def update_pos(self):
        self.x_pos += self.x_vel
        self.y_pos += self.y_vel

    def turn(self, direction):
        if direction is Snake.Directions.LEFT:
            self.y_vel = 0
            self.x_vel = -Tile.TILE_WIDTH
        elif direction is Snake.Directions.RIGHT:
            self.y_vel = 0
            self.x_vel = Tile.TILE_WIDTH
        elif direction is Snake.Directions.UP:
            self.x_vel = 0
            self.y_vel = -Tile.TILE_WIDTH
        elif direction is Snake.Directions.DOWN:
            self.x_vel = 0
            self.y_vel = Tile.TILE_WIDTH

    def draw(self, screen):
        screen.blit(self.head.tile, (self.x_pos, self.y_pos))
