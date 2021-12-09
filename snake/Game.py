import pygame

from snake.Tile import Tile
from snake.Snake import Snake

class Game:
    def __init__(self, width=100, height=100):

        # window parameters
        self.screen_w = width
        self.screen_h = height
        self.size = (width, height)
        self.logo = pygame.image.load("C:/Users/benle/PycharmProjects/Snake/resources/pythonImg1.png")
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

        # Background tiles list
        self.Tiles = []
        for x in range(int(self.screen_w / 25)):
            for y in range(int(self.screen_h / 25)):
                self.Tiles.append(Tile("Black", x=x * 25, y=y * 25))

        # Snake object
        self.snake = Snake(100, 100)

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

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        self.snake.start()
                    elif event.key == pygame.K_LEFT:
                        self.snake.turn(direction="LEFT")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.turn(direction="RIGHT")
                    elif event.key == pygame.K_UP:
                        self.snake.turn(direction="UP")
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn(direction="DOWN")
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False

            # ALL EVENT PROCESSING GOES ABOVE

            # ALL GAME LOGIC GOES BELOW

            self.snake.update_pos()

            # ALL GAME LOGIC GOES ABOVE

            # ALL CODE TO DRAW GOES BELOW

            self.screen.fill(self.white)

            for tile in self.Tiles:
                self.screen.blit(tile.tile, (tile.x_pos, tile.y_pos))

            self.snake.draw(self.screen)

            pygame.display.update()

            # ALL CODE TO DRAW GOES ABOVE

            self.clock.tick(60)
