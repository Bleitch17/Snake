from game_objects.TileBase import TileBase


class AppleTile(TileBase):
    def __init__(self, x, y):
        TileBase.__init__(self, TileBase.TileColors.RED)
        self._x_pos = x
        self._y_pos = y

    def set_pos(self, new_pos):
        self._x_pos, self._y_pos = new_pos

    def get_pos(self):
        return self._x_pos, self._y_pos

    def draw(self, screen):
        screen.blit(self._tile, (self._x_pos, self._y_pos))
