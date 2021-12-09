import pygame


class Tile:
    def __init__(self, c, Images=None, x=0, y=0):
        if Images is None:
            Images = ['C:/Users/benle/PycharmProjects/Snake/resources/Black_Tile.png',
                      'C:/Users/benle/PycharmProjects/Snake/resources/Green_Tile.png']
        self.color = c

        if self.color == "Black":
            self.image = Images[0]
        elif self.color == "Green":
            self.image = Images[1]

        self.x_pos = x
        self.y_pos = y

        self._tile = pygame.image.load(self.image)
        self._tile = pygame.transform.scale(self._tile, (25, 25))

        self.populated = False

    def populate(self, c, Images=None):
        self.color = c

        if Images is None:
            Images = ['C:/Users/benle/PycharmProjects/Snake/resources/Black_Tile.png',
                      'C:/Users/benle/PycharmProjects/Snake/resources/Green_Tile.png']

        if self.color == "Black":
            self.image = Images[0]
            self.populated = False
        elif self.color == "Green":
            self.image = Images[1]
            self.populated = True

        self._tile = pygame.image.load(self.image)
        self._tile = pygame.transform.scale(self._tile, (25, 25))

    @property
    def tile(self):
        return self._tile
