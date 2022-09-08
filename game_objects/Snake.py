from game_objects.BodyTile import BodyTile
from game_objects.Directions import Directions


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
