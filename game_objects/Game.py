import pygame

from game_objects.BackgroundTile import BackgroundTile
from game_objects.Snake import Snake


class Game:
    FRAMES_PER_SECOND = 60

    def __init__(self, width):
        self.screen_w = width
        self.size = (width, width)

        pygame.display.set_icon(pygame.image.load('./resources/pythonImg1.png'))
        pygame.display.set_caption('Snake')

        self.screen = pygame.display.set_mode(self.size)

        self.background_tiles = self.create_background()

        self.snake = Snake(100, 100)

        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        while self.running:
            # ALL EVENT PROCESSING GOES BELOW

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYUP:
                    match event.key:
                        case pygame.K_LEFT:
                            self.snake.turn(Snake.Directions.LEFT)
                        case pygame.K_RIGHT:
                            self.snake.turn(Snake.Directions.RIGHT)
                        case pygame.K_UP:
                            self.snake.turn(Snake.Directions.UP)
                        case pygame.K_DOWN:
                            self.snake.turn(Snake.Directions.DOWN)
                        case pygame.K_ESCAPE:
                            self.running = False

            # ALL EVENT PROCESSING GOES ABOVE

            # ALL GAME LOGIC GOES BELOW

            self.snake.update_pos()

            # ALL GAME LOGIC GOES ABOVE

            # ALL CODE TO DRAW GOES BELOW

            self.draw_background()

            self.snake.draw(self.screen)

            pygame.display.update()

            # ALL CODE TO DRAW GOES ABOVE

            self.clock.tick(Game.FRAMES_PER_SECOND)

    def create_background(self):
        background_tiles = []
        for x in range(int(self.screen_w / BackgroundTile.TILE_WIDTH)):
            for y in range(int(self.screen_w / BackgroundTile.TILE_WIDTH)):
                background_tiles.append(
                    BackgroundTile(BackgroundTile.TileColors.BLACK, x_pos=x * BackgroundTile.TILE_WIDTH,
                                   y_pos=y * BackgroundTile.TILE_WIDTH))
        return background_tiles

    def draw_background(self):
        for background_tile in self.background_tiles:
            background_tile.draw(self.screen)
