import pygame

from snake.Game import Game


def main():
    pygame.init()

    MyApp = Game(750, 750)
    MyApp.run()

    pygame.quit()


if __name__ == "__main__":
    main()
    