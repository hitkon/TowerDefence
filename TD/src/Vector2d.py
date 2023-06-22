
class Vector2d:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2d(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def square_distance(self, other_point):
        return (self.x - other_point.x) * (self.x - other_point.x) + (self.y - other_point.y) * (self.y - other_point.y)
