import pygame

from game_objects.Game import Game


def main():
    pygame.init()

    game = Game(800)
    game.run()

    pygame.quit()


if __name__ == "__main__":
    main()
    