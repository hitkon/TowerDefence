from Tower import Tower
from ProjectileInfo import ProjectileInfo
from Vector2d import Vector2d
import pygame


class CanonTower(Tower):

    def __init__(self, pos):
        super().__init__(attack_speed=0.5, attack_range=10, build_time=0, pos=pos, proj_info=None)

    def __init__(self, pos: Vector2d, build_time: int, proj_info: ProjectileInfo):
        super().__init__(attack_speed=0.5, attack_range=10, build_time=build_time, pos=pos, proj_info=proj_info)

    def getImage(self):
        arr_tower = pygame.image.load("images/canon.png")
        arr_tower = pygame.transform.scale(arr_tower, (50, 50))
        return arr_tower


# def getImage():
#     arr_tower = pygame.image.load("images/canon.png")
#     arr_tower = pygame.transform.scale(arr_tower, (50, 50))
#     return arr_tower