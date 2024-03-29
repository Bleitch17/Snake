import copy
from collections import deque

from game_objects.TileBase import TileBase
from game_objects.Directions import Directions


class BodyTile(TileBase):
    def __init__(self, x, y, direction, speed):
        TileBase.__init__(self, TileBase.TileColors.GREEN)
        self._x_pos = x
        self._y_pos = y
        self._direction = direction
        self._speed = speed
        self._scheduled_turns = deque()

    def clone_and_shift(self):
        new_body_tile_x, new_body_tile_y = self._x_pos, self._y_pos
        match self._direction:
            case Directions.UP:
                new_body_tile_y += TileBase.TILE_WIDTH
            case Directions.DOWN:
                new_body_tile_y -= TileBase.TILE_WIDTH
            case Directions.LEFT:
                new_body_tile_x += TileBase.TILE_WIDTH
            case Directions.RIGHT:
                new_body_tile_x -= TileBase.TILE_WIDTH

        new_body_tile = BodyTile(new_body_tile_x, new_body_tile_y, self._direction, self._speed)
        new_body_tile._scheduled_turns = copy.deepcopy(self._scheduled_turns)
        return new_body_tile

    def get_position(self):
        return self._x_pos, self._y_pos

    def get_direction(self):
        return self._direction

    def get_last_turn(self):
        return self._scheduled_turns[-1]

    def has_scheduled_turn(self):
        return len(self._scheduled_turns) > 0

    def update_pos(self):
        match self._direction:
            case Directions.LEFT:
                self._x_pos -= self._speed
            case Directions.RIGHT:
                self._x_pos += self._speed
            case Directions.UP:
                self._y_pos -= self._speed
            case Directions.DOWN:
                self._y_pos += self._speed

    def schedule_turn(self, turn):
        self._scheduled_turns.append(turn)

    def process_next_turn(self):
        if (self._x_pos, self._y_pos) == self._scheduled_turns[0].get_pos():
            self._direction = self._scheduled_turns.popleft().get_direction()

    def draw(self, screen):
        screen.blit(self._tile, (self._x_pos, self._y_pos))
