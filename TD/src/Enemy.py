from Entity import Entity
from EnemyRoad import EnemyRoad
from Vector2d import Vector2d


class Enemy(Entity):

    direction = {"W": 0, "N": 1, "E": 2, "S": 3}
    MAX_DIRECTIONS = 4

    def __init__(self):
        self.direction = "W"
        self.reward_items = []
        self.score_reward = 0
        self.road = None

    def __init__(self, type):
        pass

    def __init__(self, direction, reward_items, score_reward, road: EnemyRoad):
        super().__init__(10, None, None)
        self.direction = direction
        self.reward_items = reward_items
        self.score_reward = score_reward
        self.road = road

    def get_left_direction(self):
        if self.direction == "W":
            return "S"
        elif self.direction == "N":
            return "W"
        elif self.direction == "E":
            return "N"
        elif self.direction == "S":
            return "E"

    def get_right_direction(self):
        if self.direction == "W":
            return "N"
        elif self.direction == "N":
            return "E"
        elif self.direction == "E":
            return "S"
        elif self.direction == "S":
            return "W"

    def get_forward_pos(self):
        if self.direction == "N":
            return self.pos + Vector2d(0, 1)
        elif self.direction == "W":
            return self.pos + Vector2d(-1, 0)
        elif self.direction == "E":
            return self.pos + Vector2d(1, 0)
        elif self.direction == "S":
            return self.pos + Vector2d(0, -1)

    def move(self):
        next_move = self.road.next_move()
        if next_move is None:
            return False
        if next_move == "l":
            self.direction = self.get_left_direction()
        elif next_move == "r":
            self.direction = self.get_right_direction()
        elif next_move == "f":
            self.pos = self.get_forward_pos()
        return True
