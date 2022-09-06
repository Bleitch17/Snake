from game_objects.TileBase import TileBase
from game_objects.Directions import Directions


class Snake:
    allowed_next_turn_directions = {
        Directions.LEFT: [Directions.UP, Directions.DOWN],
        Directions.RIGHT: [Directions.UP, Directions.DOWN],
        Directions.UP: [Directions.LEFT, Directions.RIGHT],
        Directions.DOWN: [Directions.LEFT, Directions.RIGHT]
    }

    velocity = 2

    def __init__(self, x=0, y=0):
        self.x_pos = x
        self.y_pos = y

        self.direction = Directions.RIGHT

        self.length = 1

        self.head = TileBase(TileBase.TileColors.GREEN)

    def get_head_position(self):
        return self.x_pos, self.y_pos

    def get_head_direction(self):
        return self.direction

    def set_head_direction(self, direction):
        self.direction = direction

    def get_length(self):
        return self.length

    def update_pos(self):
        match self.direction:
            case Directions.LEFT:
                self.x_pos -= Snake.velocity
            case Directions.RIGHT:
                self.x_pos += Snake.velocity
            case Directions.UP:
                self.y_pos -= Snake.velocity
            case Directions.DOWN:
                self.y_pos += Snake.velocity

    def draw(self, screen):
        screen.blit(self.head.tile, (self.x_pos, self.y_pos))
