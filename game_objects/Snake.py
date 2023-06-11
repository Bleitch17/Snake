from game_objects.BodyTile import BodyTile
from game_objects.Directions import Directions
from game_objects.Turn import Turn
from game_settings.GameSettings import SNAKE_INITIAL_X, SNAKE_INITIAL_Y


INITIAL_LENGTH = 3

VALID_NEXT_TURN_DIRECTIONS = {
    Directions.LEFT: [Directions.UP, Directions.DOWN],
    Directions.RIGHT: [Directions.UP, Directions.DOWN],
    Directions.UP: [Directions.LEFT, Directions.RIGHT],
    Directions.DOWN: [Directions.LEFT, Directions.RIGHT]
}


def create_body(x, y, direction, speed):
    return [BodyTile(x - (i * BodyTile.TILE_WIDTH), y, direction, speed) for i in range(INITIAL_LENGTH)]


class Snake:
    def __init__(self, speed, direction, x=SNAKE_INITIAL_X, y=SNAKE_INITIAL_Y):
        self._body = create_body(x, y, direction, speed)

    def update_pos(self):
        for body_segment in self._body:
            body_segment.update_pos()

    def process_turns(self):
        # Only process turns for the body segments that have them
        segment_with_turn_index = -1
        for i in range(len(self._body)):
            if self._body[i].has_scheduled_turn():
                segment_with_turn_index = i
                break

        if segment_with_turn_index < 0:
            return

        for i in range(segment_with_turn_index, len(self._body)):
            self._body[i].process_next_turn()

    def schedule_turn(self, direction):
        if self._body[0].has_scheduled_turn():
            # TODO: Schedule turns in advance for smoother controls
            return

        current_head_direction = self._body[0].get_direction()
        if direction not in VALID_NEXT_TURN_DIRECTIONS[current_head_direction]:
            return

        current_head_position = self._body[0].get_position()

        next_turn_x = (current_head_position[0] // BodyTile.TILE_WIDTH) * BodyTile.TILE_WIDTH
        next_turn_y = (current_head_position[1] // BodyTile.TILE_WIDTH) * BodyTile.TILE_WIDTH

        match current_head_direction:
            case Directions.LEFT:
                next_turn_x -= BodyTile.TILE_WIDTH
            case Directions.RIGHT:
                next_turn_x += BodyTile.TILE_WIDTH
            case Directions.UP:
                next_turn_y -= BodyTile.TILE_WIDTH
            case Directions.DOWN:
                next_turn_y += BodyTile.TILE_WIDTH

        for body_segment in self._body:
            body_segment.schedule_turn(Turn(next_turn_x, next_turn_y, direction))

    def draw(self, screen):
        for body_segment in self._body:
            body_segment.draw(screen)
