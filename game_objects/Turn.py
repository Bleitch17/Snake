class Turn:
    def __init__(self, x, y, direction):
        self._x_pos = x
        self._y_pos = y
        self._direction = direction

    def get_pos(self):
        return self._x_pos, self._y_pos

    def get_direction(self):
        return self._direction
