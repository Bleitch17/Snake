from game_objects.TileBase import TileBase


class BackgroundTile(TileBase):
    def __init__(self, tile_color, x_pos, y_pos):
        TileBase.__init__(self, tile_color)
        self.x_pos = x_pos
        self.y_pos = y_pos

    def draw(self, screen):
        screen.blit(self._tile, (self.x_pos, self.y_pos))
