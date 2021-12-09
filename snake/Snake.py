import pygame

from snake.Tile import Tile


class Snake:
    def __init__(self, x=0, y=0):
        # Initial head position
        self.x_pos = x
        self.y_pos = y

        self.real_x_pos = x
        self.real_y_pos = y

        # Initial length of the body, excluding the head
        self.length = 0

        # The head tile:
        self.head = Tile("Green", x=x, y=y)

        # Initial head velocities (Snake is not moving until game is started):
        self.x_vel = 0
        self.y_vel = 0

        # Add a list of tiles for the body later

    def start(self):
        self.x_vel = 2.5

    def update_pos(self):
        self.real_x_pos += self.x_vel
        self.real_y_pos += self.y_vel
        if self.x_vel < 0:
            if abs(self.x_pos - self.real_x_pos) > 25:
                self.x_pos += -25
        elif self.x_vel > 0:
            if abs(self.x_pos - self.real_x_pos) > 25:
                self.x_pos += 25
        elif self.y_vel < 0:
            if abs(self.y_pos - self.real_y_pos) > 25:
                self.y_pos += -25
        elif self.y_vel > 0:
            if abs(self.y_pos - self.real_y_pos) > 25:
                self.y_pos += 25

    def turn(self, direction):
        if direction == "LEFT":
            if self.y_vel != 0:
                self.real_y_pos = self.y_pos
                self.y_vel = 0
                self.x_vel = -2.5

        elif direction == "RIGHT":
            if self.y_vel != 0:
                self.real_y_pos = self.y_pos
                self.y_vel = 0
                self.x_vel = 2.5

        elif direction == "UP":
            if self.x_vel != 0:
                self.real_x_pos = self.x_pos
                self.x_vel = 0
                self.y_vel = -2.5

        elif direction == "DOWN":
            if self.x_vel != 0:
                self.real_x_pos = self.x_pos
                self.x_vel = 0
                self.y_vel = 2.5


    def draw(self, screen):
        screen.blit(self.head.tile, (self.x_pos, self.y_pos))