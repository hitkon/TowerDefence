from Enemy import Enemy
from Skeleton import Skeleton

class EnemyGenerator:

    def __init__(self, inputLine):
        self.enemies = []
        self.current_ind = 0
        for i in inputLine:
            if i == 'a':
                self.enemies.append(Skeleton("E", [], 0, None))

    #def __init__(self, ):

    def next_enemy(self):
        if self.current_ind == len(self.enemies):
            return None
        self.current_ind += 1
        return self.enemies[self.current_ind-1]