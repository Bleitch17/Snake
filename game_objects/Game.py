import pygame

from game_objects.Tile import Tile
from game_objects.Snake import Snake


class Game:
    FRAMES_PER_SECOND = 60
    SNAKE_UPDATE_FREQUENCY = 4

    def __init__(self, width):
        self.screen_w = width
        self.size = (width, width)

        pygame.display.set_icon(pygame.image.load('./resources/pythonImg1.png'))
        pygame.display.set_caption("Snake")

        self.screen = pygame.display.set_mode(self.size)

        self.background_tiles = self.create_background()

        self.snake = Snake(100, 100)

        self.running = True
        self.clock = pygame.time.Clock()

    def run(self):
        snake_update_frame_counter = 0

        while self.running:
            # ALL EVENT PROCESSING GOES BELOW

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.snake.turn(Snake.Directions.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.turn(Snake.Directions.RIGHT)
                    elif event.key == pygame.K_UP:
                        self.snake.turn(Snake.Directions.UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.turn(Snake.Directions.DOWN)
                    elif event.key == pygame.K_ESCAPE:
                        self.running = False

            # ALL EVENT PROCESSING GOES ABOVE

            # ALL GAME LOGIC GOES BELOW

            if snake_update_frame_counter % (Game.FRAMES_PER_SECOND / Game.SNAKE_UPDATE_FREQUENCY) == 0:
                self.snake.update_pos()

            # ALL GAME LOGIC GOES ABOVE

            # ALL CODE TO DRAW GOES BELOW

            self.draw_background()

            self.snake.draw(self.screen)

            pygame.display.update()

            # ALL CODE TO DRAW GOES ABOVE

            self.clock.tick(Game.FRAMES_PER_SECOND)
            snake_update_frame_counter += 1
            snake_update_frame_counter %= Game.FRAMES_PER_SECOND

    def create_background(self):
        background_tiles = []
        for x in range(int(self.screen_w / Tile.TILE_WIDTH)):
            for y in range(int(self.screen_w / Tile.TILE_WIDTH)):
                background_tiles.append(Tile(Tile.TileColors.BLACK,
                                             x_pos=x * Tile.TILE_WIDTH,
                                             y_pos=y * Tile.TILE_WIDTH))
        return background_tiles

    def draw_background(self):
        for background_tile in self.background_tiles:
            self.screen.blit(background_tile.tile, (background_tile.x_pos, background_tile.y_pos))
