from game_objects.TileBase import TileBase
from game_objects.Game import Directions


class BodyTile(TileBase):
    def __init__(self, x, y, direction, speed):
        TileBase.__init__(self, TileBase.TileColors.GREEN)
        self.x_pos = x
        self.y_pos = y
        self.direction = direction
        self.speed = speed

    def get_position(self):
        return self.x_pos, self.y_pos

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def update_pos(self):
        match self.direction:
            case Directions.LEFT:
                self.x_pos -= self.speed
            case Directions.RIGHT:
                self.x_pos += self.speed
            case Directions.UP:
                self.y_pos -= self.speed
            case Directions.DOWN:
                self.y_pos += self.speed

    def draw(self, screen):
        screen.blit(self._tile, (self.x_pos, self.y_pos))
