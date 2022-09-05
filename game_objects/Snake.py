from enum import Enum

from game_objects.TileBase import TileBase


class Snake:
    class Directions(Enum):
        LEFT = 0
        RIGHT = 1
        UP = 2
        DOWN = 3

    velocity = 2

    def __init__(self, x=0, y=0):
        self.x_pos = x
        self.y_pos = y

        self.direction = Snake.Directions.RIGHT
        self.next_direction = Snake.Directions.RIGHT
        self.turn_point = None

        self.length = 1

        self.head = TileBase(TileBase.TileColors.GREEN)

        # TODO: list of tiles for the body, initially start at length 1

    def update_pos(self):
        if self.turn_point is not None and self.x_pos == self.turn_point[0] and self.y_pos == self.turn_point[1]:
            self.direction = self.next_direction
            self.turn_point = None

        match self.direction:
            case Snake.Directions.LEFT:
                self.x_pos -= Snake.velocity
            case Snake.Directions.RIGHT:
                self.x_pos += Snake.velocity
            case Snake.Directions.UP:
                self.y_pos -= Snake.velocity
            case Snake.Directions.DOWN:
                self.y_pos += Snake.velocity

    def turn(self, direction):
        if direction is Snake.Directions.LEFT and self.direction is not Snake.Directions.RIGHT:
            self.next_direction = Snake.Directions.LEFT
        elif direction is Snake.Directions.RIGHT and self.direction is not Snake.Directions.LEFT:
            self.next_direction = Snake.Directions.RIGHT
        elif direction is Snake.Directions.UP and self.direction is not Snake.Directions.DOWN:
            self.next_direction = Snake.Directions.UP
        elif direction is Snake.Directions.DOWN and self.direction is not Snake.Directions.UP:
            self.next_direction = Snake.Directions.DOWN

        if self.turn_point is None:
            self.set_turn_point()

    def set_turn_point(self):
        match self.direction:
            case Snake.Directions.LEFT:
                self.turn_point = (self.x_pos - (self.x_pos % TileBase.TILE_WIDTH), self.y_pos)
            case Snake.Directions.RIGHT:
                self.turn_point = (self.x_pos + TileBase.TILE_WIDTH - (self.x_pos % TileBase.TILE_WIDTH), self.y_pos)
            case Snake.Directions.UP:
                self.turn_point = (self.x_pos, self.y_pos - (self.y_pos % TileBase.TILE_WIDTH))
            case Snake.Directions.DOWN:
                self.turn_point = (self.x_pos, self.y_pos + TileBase.TILE_WIDTH - (self.y_pos % TileBase.TILE_WIDTH))

    def draw(self, screen):
        screen.blit(self.head.tile, (self.x_pos, self.y_pos))
