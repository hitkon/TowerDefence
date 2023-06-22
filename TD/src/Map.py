import random

from MapCell import MapCell
from Vector2d import Vector2d
from EnemyGenerator import EnemyGenerator
from EnemyRoad import EnemyRoad
from Entity import Entity

import sys

class Map:
    def road_validation(road_line):
        pass


    def __init__(self, filename: str):

        with open(filename, "r") as inp:
            str = inp.readline()
            words = str.split()
            self.width = int(words[0])
            self.height = int(words[1])
            self.field = []
            for j in range(self.height):
                line = inp.readline()
                row = []
                for i in range(self.width):
                    pos = Vector2d(i,j)
                    row.append(MapCell(pos, int(line[i])))
                self.field.append(row)
            enemy_generator_amount = int(inp.readline())
            self.enemy_generator = []
            for i in range(enemy_generator_amount):
                self.enemy_generator.append(EnemyGenerator(inp.readline()))
            enemy_roads_amount = int(inp.readline())
            self.enemy_roads = []
            for i in range(enemy_roads_amount):
                pos_line = inp.readline().split(" ")
                start_pos = Vector2d(int(pos_line[0]), int(pos_line[1]))
                self.enemy_roads.append(EnemyRoad(inp.readline(), start_pos))

    def add(self, obj: Entity):
        if self.field[obj.pos.x][obj.pos.y].entity is None:
            raise ValueError(str(self.field[obj.pos.x][obj.pos.y].entity) + "is occupied")
        self.field[obj.pos.x][obj.pos.y].add_entity(obj)

    def is_occupied(self, pos: Vector2d):
        return self.field[pos.x][pos.y] is None

    def remove(self, pos: Vector2d):
        self.field[pos.x][pos.y].remove_entity()

    def get_cell(self, pos: Vector2d):
        return self.field[pos.x][pos.y]

    def get_random_enemeny_list(self):
        """Get one of the generators"""
        return self.enemy_generator[random.randint(0, len(self.enemy_generator) - 1)]

    def get_random_enemy_road(self):
        """Get one of the roads"""
        return self.enemy_roads[random.randint(0, len(self.enemy_roads) - 1)]
