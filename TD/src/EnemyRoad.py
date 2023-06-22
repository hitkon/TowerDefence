from Vector2d import Vector2d

class EnemyRoad:
    directions = {"f": 0, "r": 1, "l": 2}

    def __init__(self, road_line, start_pos):
        self.current_ind = 0
        self.start_position = start_pos
        self.road = list(road_line)

    def next_move(self):
        if self.current_ind == len(self.road):
            return None
        self.current_ind += 1
        return self.road[self.current_ind-1]