import pygame

from game_objects.Directions import Directions
from game_objects.BackgroundTile import BackgroundTile
from game_objects.Snake import Snake
from game_objects.TurnMarker import TurnMarker


class Game:
    FRAMES_PER_SECOND = 60
    SNAKE_SPEED = 2
    SNAKE_INITIAL_X = 100
    SNAKE_INITIAL_Y = 100
    SNAKE_INITIAL_DIRECTION = Directions.RIGHT

    def __init__(self, width):
        self.screen_w = width
        self.size = (width, width)

        pygame.display.set_icon(pygame.image.load('./resources/pythonImg1.png'))
        pygame.display.set_caption('Snake')

        self.screen = pygame.display.set_mode(self.size)

        self.background_tiles = self.create_background()
        self.snake = Snake(Game.SNAKE_SPEED, Game.SNAKE_INITIAL_DIRECTION, Game.SNAKE_INITIAL_X, Game.SNAKE_INITIAL_Y)
        self.turn_markers = []

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
                            self.place_turn_marker(Directions.LEFT)
                        case pygame.K_RIGHT:
                            self.place_turn_marker(Directions.RIGHT)
                        case pygame.K_UP:
                            self.place_turn_marker(Directions.UP)
                        case pygame.K_DOWN:
                            self.place_turn_marker(Directions.DOWN)
                        case pygame.K_ESCAPE:
                            self.running = False

            # ALL EVENT PROCESSING GOES ABOVE

            # ALL GAME LOGIC GOES BELOW

            # TODO: confirm this is safe with body longer than just head
            for turn_marker in self.turn_markers[::-1]:
                if turn_marker.is_position_equal_to_other_position(self.snake.get_head_position()):
                    self.snake.set_head_direction(turn_marker.get_turn_direction())
                    turn_marker.decrement_remaining_turns()
                    if turn_marker.get_remaining_turns() == 0:
                        self.turn_markers.remove(turn_marker)

            self.snake.update_pos()

            # ALL GAME LOGIC GOES ABOVE

            # ALL CODE TO DRAW GOES BELOW

            self.draw_background()

            self.snake.draw(self.screen)

            pygame.display.update()

            # ALL CODE TO DRAW GOES ABOVE

            self.clock.tick(Game.FRAMES_PER_SECOND)

    def place_turn_marker(self, turn_direction):
        snake_position = self.snake.get_head_position()
        snake_direction = self.snake.get_head_direction()

        if turn_direction in Snake.allowed_next_turn_directions[snake_direction]:
            turn_marker = TurnMarker(snake_position[0], snake_position[1], snake_direction, turn_direction,
                                     self.snake.get_length())
            self.add_turn_marker(turn_marker)

    def add_turn_marker(self, new_turn_marker):
        if len(self.turn_markers) == 0:
            self.turn_markers.append(new_turn_marker)
        else:
            existing_marker_index = self.get_index_of_marker_by_position(new_turn_marker.get_position())
            if existing_marker_index >= 0:
                self.turn_markers[existing_marker_index].set_turn_direction(new_turn_marker.get_turn_direction())
            else:
                self.turn_markers.append(new_turn_marker)

    def get_index_of_marker_by_position(self, position):
        for i in range(len(self.turn_markers)):
            if self.turn_markers[i].is_position_equal_to_other_position(position):
                return i
        return -1

    def create_background(self):
        background_tiles = []
        for x in range(int(self.screen_w / BackgroundTile.TILE_WIDTH)):
            for y in range(int(self.screen_w / BackgroundTile.TILE_WIDTH)):
                background_tiles.append(
                    BackgroundTile(x * BackgroundTile.TILE_WIDTH, y * BackgroundTile.TILE_WIDTH))
        return background_tiles

    def draw_background(self):
        for background_tile in self.background_tiles:
            background_tile.draw(self.screen)
