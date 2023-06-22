
# from src.MapCell import MapCell

import sys

sys.path.insert(0, "src/")
from src.Map import Map
from src.ArrowTower import ArrowTower
from src.CanonTower import CanonTower
from src.Vector2d import Vector2d
from src.Projectile import Projectile
from src.ProjectileInfo import ProjectileInfo
from src.Skeleton import Skeleton
from src.EnemyRoad import EnemyRoad
from src.Engine import Engine
from src.Gui import Gui

import unittest

# class Tests(unittest.TestCase):
#
#     def test_projectile_reach_target(self):
#         A = ArrowTower(pos=Vector2d(2, 0), build_time=0)
#         B = ArrowTower(pos=Vector2d(4, 4), build_time=0)
#         P = Projectile(ProjectileInfo(damage=10, speed=20), A.pos, B, A)
#         self.assertTrue(P.move())
#
#     def test_projectile_reach_target_in_3_turns(self):
#         A = ArrowTower(pos=Vector2d(2, 0), build_time=0)
#         B = ArrowTower(pos=Vector2d(4, 4), build_time=0)
#         P = Projectile(ProjectileInfo(damage=10, speed=5), A.pos, B, A)
#         self.assertFalse(P.move())
#         print(P.position)
#         self.assertFalse(P.move())
#         print(P.position)
#         self.assertTrue(P.move())
#
#     def test_enemy_move(self):
#         road = "flrfrf"
#         A = Skeleton(Vector2d(0, 0), EnemyRoad(road))
#         self.assertEqual(A.direction, "N")
#         A.move()
#         self.assertEqual(A.pos, Vector2d(0, 1))
#         A.move()
#         self.assertEqual(A.direction, "W")
#         A.move()
#         self.assertEqual(A.direction, "N")
#         A.move()
#         self.assertEqual(A.pos, Vector2d(0, 2))
#         A.move()
#         A.move()
#         self.assertEqual(A.pos, Vector2d(1, 2))
#
#     def test_map(self):
#         pass


if __name__ == '__main__':
    print("HI")
    app = Gui()

    # unittest.main()
    # pass
