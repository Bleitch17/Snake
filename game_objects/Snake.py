from game_objects.BodyTile import BodyTile
from game_objects.Directions import Directions
from game_objects.TurnMarker import TurnMarker


def attempt_to_turn_body_segment_if_at_turn_marker(turn_marker: TurnMarker, body_segment: BodyTile):
    if turn_marker.is_position_equal_to_other_position(body_segment.get_position()) and \
            turn_marker.get_remaining_turns() > 0:
        body_segment.set_direction(turn_marker.get_turn_direction())
        turn_marker.decrement_remaining_turns()


class Snake:
    allowed_next_turn_directions = {
        Directions.LEFT: [Directions.UP, Directions.DOWN],
        Directions.RIGHT: [Directions.UP, Directions.DOWN],
        Directions.UP: [Directions.LEFT, Directions.RIGHT],
        Directions.DOWN: [Directions.LEFT, Directions.RIGHT]
    }

    def __init__(self, speed, direction, x=100, y=100):
        self.head = BodyTile(x, y, direction, speed)
        self.length = 3
        self.tail = self.create_tail(self.length, speed)

    def get_head_position(self):
        return self.head.get_position()

    def get_head_direction(self):
        return self.head.get_direction()

    def set_head_direction(self, direction):
        self.head.set_direction(direction)

    def get_length(self):
        return self.length

    def get_tail(self):
        return self.tail

    def process_turn_marker(self, turn_marker: TurnMarker):
        attempt_to_turn_body_segment_if_at_turn_marker(turn_marker, self.head)
        for tail_segment in self.tail:
            attempt_to_turn_body_segment_if_at_turn_marker(turn_marker, tail_segment)

    def update_pos(self):
        self.head.update_pos()
        for tail_segment in self.tail:
            tail_segment.update_pos()

    def draw(self, screen):
        self.head.draw(screen)
        for tail_segment in self.tail:
            tail_segment.draw(screen)

    def create_tail(self, body_length, speed):
        body = []
        initial_head_position = self.head.get_position()
        for i in range(1, body_length):
            body.append(BodyTile(initial_head_position[0] - (i * BodyTile.TILE_WIDTH), initial_head_position[1],
                                 self.head.get_direction(), speed))
        return body
