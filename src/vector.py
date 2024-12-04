class Vector2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def get_dimensions(self):
        return (self.x, self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
