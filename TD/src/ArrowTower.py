from Tower import Tower
from Vector2d import Vector2d
from ProjectileInfo import ProjectileInfo
import pygame

class ArrowTower(Tower):

    def __init__(self, pos):
        super().__init__(attack_speed=0.5, attack_range=10, build_time=0, pos=pos, proj_info=None)

    def __init__(self, pos: Vector2d, build_time: int, proj_info: ProjectileInfo):
        super().__init__(attack_speed=0.5, attack_range=10, build_time=build_time, pos=pos, proj_info=proj_info)
        #self.projectile_info = proj_info
        # self.hp = 10
        # self.pos = pos

    def getImage(self):
        arr_tower = pygame.image.load("images/ArrowTower.jpg")
        arr_tower = pygame.transform.scale(arr_tower, (50, 50))
        return arr_tower

# def getImage():
#     arr_tower = pygame.image.load("images/ArrowTower.jpg")
#     arr_tower = pygame.transform.scale(arr_tower, (50, 50))
#     return arr_tower