from game_objects.TileBase import TileBase


class BackgroundTile(TileBase):
    def __init__(self, x, y):
        TileBase.__init__(self, TileBase.TileColors.BLACK)
        self.x_pos = x
        self.y_pos = y

    def draw(self, screen):
        screen.blit(self._tile, (self.x_pos, self.y_pos))
