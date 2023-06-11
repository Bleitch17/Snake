from game_objects.BodyTile import BodyTile
from game_objects.TileBase import TileBase
from game_objects.Directions import Directions
from game_objects.Turn import Turn
from game_settings.GameSettings import SNAKE_INITIAL_X, SNAKE_INITIAL_Y, WIDTH

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

    def get_head_pos(self):
        return self._body[0].get_position()

    def update_pos(self):
        for body_segment in self._body:
            body_segment.update_pos()

    def extend_tail(self):
        self._body.append(self._body[len(self._body) - 1].clone_and_shift())

    def collides_with_snake(self, other_pos):
        for body_tile in self._body:
            tile_position = body_tile.get_position()
            if other_pos[0] <= tile_position[0] <= other_pos[0] + TileBase.TILE_WIDTH \
                    and other_pos[1] <= tile_position[1] <= other_pos[1] + TileBase.TILE_WIDTH:
                return True
        return False

    def is_alive(self):
        head_pos = self.get_head_pos()
        if head_pos[0] < 0 or head_pos[0] >= WIDTH or head_pos[1] < 0 or head_pos[1] >= WIDTH:
            return False

        for body_tile in self._body[3:]:
            tile_pos = body_tile.get_position()
            if head_pos[0] <= tile_pos[0] <= head_pos[0] + TileBase.TILE_WIDTH \
                    and head_pos[1] <= tile_pos[1] <= head_pos[1] + TileBase.TILE_WIDTH:
                return False
        return True

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
            last_turn = self._body[0].get_last_turn()
            last_turn_direction = last_turn.get_direction()
            if direction not in VALID_NEXT_TURN_DIRECTIONS[last_turn_direction]:
                return

            next_turn_x, next_turn_y = last_turn.get_pos()

            match last_turn_direction:
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
