from game_objects.Directions import Directions
from game_objects.TileBase import TileBase


class TurnMarker:
    def __init__(self, x, y, object_direction, turn_direction, remaining_turns):
        self._turn_direction = turn_direction
        self._remaining_turns = remaining_turns

        match object_direction:
            case Directions.LEFT:
                self._x_pos = x - (x % TileBase.TILE_WIDTH)
                self._y_pos = y
            case Directions.RIGHT:
                self._x_pos = x + TileBase.TILE_WIDTH - (x % TileBase.TILE_WIDTH)
                self._y_pos = y
            case Directions.UP:
                self._x_pos = x
                self._y_pos = y - (y % TileBase.TILE_WIDTH)
            case Directions.DOWN:
                self._x_pos = x
                self._y_pos = y + TileBase.TILE_WIDTH - (y % TileBase.TILE_WIDTH)

    def get_position(self):
        return self._x_pos, self._y_pos

    def get_turn_direction(self):
        return self._turn_direction

    def set_turn_direction(self, direction):
        self._turn_direction = direction

    def get_remaining_turns(self):
        return self._remaining_turns

    def decrement_remaining_turns(self):
        self._remaining_turns -= 1

    def is_position_equal_to_other_position(self, other_marker_position):
        return self.get_position()[0] == other_marker_position[0] and self.get_position()[1] == other_marker_position[1]
