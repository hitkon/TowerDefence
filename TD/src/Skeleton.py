from Enemy import Enemy
from EnemyRoad import EnemyRoad
import pygame

class Skeleton(Enemy):

    def __init__(self, pos, enemy_road):
        super().__init__("N", [], 10, enemy_road)
        self.hp = 10
        self.pos = pos
        self.target = None
        self.projectile_info = None

    def getImage(self):
        image = pygame.image.load("images/skeleton.jpg")
        image = pygame.transform.scale(image, (50, 50))
        return image

    def __init__(self, direction, reward_items, score_reward, road: EnemyRoad):
        super().__init__(direction, reward_items, score_reward, road)

