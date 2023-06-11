import pygame
import random

from game_objects.TileBase import TileBase
from game_objects.Directions import Directions
from game_objects.BackgroundTile import BackgroundTile
from game_objects.Snake import Snake
from game_objects.AppleTile import AppleTile
from game_settings.GameSettings import WIDTH, SNAKE_SPEED, SNAKE_INITIAL_X, SNAKE_INITIAL_Y, SNAKE_INITIAL_DIRECTION, \
    FRAMES_PER_SECOND


def check_tile_collision(tile_pos, other_tile_pos):
    return tile_pos[0] <= other_tile_pos[0] <= tile_pos[0] + TileBase.TILE_WIDTH \
        and tile_pos[1] <= other_tile_pos[1] <= tile_pos[1] + TileBase.TILE_WIDTH


class Game:
    def __init__(self):
        self.screen_w = WIDTH
        self.size = (WIDTH, WIDTH)

        pygame.display.set_icon(pygame.image.load('./resources/pythonImg1.png'))
        pygame.display.set_caption('Snake')

        self.screen = pygame.display.set_mode(self.size)

        self.background_tiles = self.create_background()
        self.snake = Snake(SNAKE_SPEED, SNAKE_INITIAL_DIRECTION, SNAKE_INITIAL_X, SNAKE_INITIAL_Y)
        self.apple = AppleTile(200, 200)

        self.draw_game_objects()

        self.running = True
        self.clock = pygame.time.Clock()

    def run(self) -> None:
        while self.running:
            # ALL EVENT PROCESSING GOES BELOW

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYUP:
                    match event.key:
                        case pygame.K_LEFT:
                            self.snake.schedule_turn(Directions.LEFT)
                        case pygame.K_RIGHT:
                            self.snake.schedule_turn(Directions.RIGHT)
                        case pygame.K_UP:
                            self.snake.schedule_turn(Directions.UP)
                        case pygame.K_DOWN:
                            self.snake.schedule_turn(Directions.DOWN)
                        case pygame.K_ESCAPE:
                            self.running = False

            # ALL EVENT PROCESSING GOES ABOVE

            # ALL GAME LOGIC GOES BELOW

            self.snake.update_pos()
            self.snake.process_turns()

            # Check collisions:
            if check_tile_collision(self.apple.get_pos(), self.snake.get_head_pos()):

                self.apple.set_pos(((random.randint(0, WIDTH) // TileBase.TILE_WIDTH) * TileBase.TILE_WIDTH,
                                    (random.randint(0, WIDTH) // TileBase.TILE_WIDTH) * TileBase.TILE_WIDTH))
                while self.snake.collides_with_snake(self.apple.get_pos()):
                    self.apple.set_pos(((random.randint(0, WIDTH) // TileBase.TILE_WIDTH) * TileBase.TILE_WIDTH,
                                        (random.randint(0, WIDTH) // TileBase.TILE_WIDTH) * TileBase.TILE_WIDTH))
                self.snake.extend_tail()

            if not self.snake.is_alive():
                self.running = False
                break

            # ALL GAME LOGIC GOES ABOVE

            # ALL CODE TO DRAW GOES BELOW

            self.draw_game_objects()

            pygame.display.update()

            # ALL CODE TO DRAW GOES ABOVE

            self.clock.tick(FRAMES_PER_SECOND)

    def draw_game_objects(self):
        # Order:
        # 1. Background
        # 2. Apple
        # 3. Snake

        for background_tile in self.background_tiles:
            background_tile.draw(self.screen)

        self.apple.draw(self.screen)
        self.snake.draw(self.screen)

    def create_background(self):
        return [BackgroundTile(x * BackgroundTile.TILE_WIDTH, y * BackgroundTile.TILE_WIDTH)
                for x in range(int(self.screen_w / BackgroundTile.TILE_WIDTH))
                for y in range(int(self.screen_w / BackgroundTile.TILE_WIDTH))]
