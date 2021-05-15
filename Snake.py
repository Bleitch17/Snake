import pygame


class Tile:
    def __init__(self, c, Images=['Black_Tile.png', 'Green_Tile.png'], x=0, y=0):
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
            Images = ['Black_Tile.png', 'Green_Tile.png']

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


class Game:
    def __init__(self, width=100, height=100):

        # window parameters
        self.screen_w = width
        self.screen_h = height
        self.size = (width, height)
        self.logo = pygame.image.load("pythonImg1.png")
        pygame.display.set_icon(self.logo)
        pygame.display.set_caption("Snake")

        # mouse variables
        self.mouse_x = 0
        self.mouse_y = 0

        # colors
        self.black = 0, 0, 0
        self.white = 255, 255, 255

        # surfaces
        self.screen = pygame.display.set_mode(self.size)

        # object lists
        self.Tiles = []
        for x in range(int(self.screen_w / 25)):
            for y in range(int(self.screen_h / 25)):
                self.Tiles.append(Tile("Black", x=x * 25, y=y * 25))

        # game loop controls
        self.running = False
        self.clock = pygame.time.Clock()

    def run(self, r=True):
        # variable controlling main loop
        self.running = r
        # main loop
        while self.running:
            # ALL EVENT PROCESSING GOES BELOW

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

                    for tile in self.Tiles:
                        if (tile.x_pos <= self.mouse_x < tile.x_pos + 25 and
                                tile.y_pos <= self.mouse_y < tile.y_pos + 25):

                            if not tile.populated:
                                tile.populate("Green")
                            else:
                                tile.populate("Black")

            # ALL EVENT PROCESSING GOES ABOVE

            # ALL GAME LOGIC GOES BELOW

            # ALL GAME LOGIC GOES ABOVE

            # ALL CODE TO DRAW GOES BELOW

            self.screen.fill(self.white)

            for tile in self.Tiles:
                self.screen.blit(tile.tile, (tile.x_pos, tile.y_pos))

            pygame.display.update()

            # ALL CODE TO DRAW GOES ABOVE

            self.clock.tick(60)


def main():
    pygame.init()

    MyApp = Game(300, 300)
    MyApp.run()

    pygame.quit()


if __name__ == "__main__":
    main()
