import copy

from Vector2d import Vector2d
from EnemyGenerator import EnemyGenerator
from EnemyRoad import EnemyRoad
from Map import Map
from ArrowTower import ArrowTower
from Tower import Tower
from ProjectileInfo import ProjectileInfo


class Engine:
    def __init__(self, map: Map):
        self.map = map
        self.enemy_generator = map.get_random_enemeny_list()
        self.enemy_list = []
        self.tower_list = []
        self.projectile_list = []
        self.iteration_num = 0
        self.enemy_passed = 0
        self.delay = 120
        self.enemy_killed = 0


    def addTower(self, tower: Tower):
        self.tower_list.append(tower)

    def run(self):
        while True:
            print(self.iteration_num, self.enemy_passed)

            if self.iteration_num % 4 == 0:
                for tower in self.tower_list:
                    if tower.target is None:
                        tower.find_target(self.enemy_list)
                    proj = tower.attack()
                    if proj is None:
                        print("No Attack")
                    else:
                        self.projectile_list.append(proj)

            if self.iteration_num % 2 == 0:
                for proj in self.projectile_list:
                    proj.move()


            if self.iteration_num % 3 == 0:
                for enemy in self.enemy_list:
                    #print(self.map.get_random_enemy_road().road)
                    if not enemy.move():
                        #print(self.map.get_random_enemy_road().road)
                        #print(enemy.road.road)
                        self.enemy_passed += 1

                        self.enemy_list.remove(enemy)
                    else:
                        print(enemy.pos, end=" ")
                print()

            if self.iteration_num % 9 == 0:
                new_enemy = self.enemy_generator.next_enemy()
                if new_enemy is None:
                    if len(self.enemy_list) == 0:
                        print(self.enemy_list)
                        print("End of Enemies")
                        break
                    #print("End of Enemy list")
                else:
                    new_enemy.road = copy.deepcopy(self.map.get_random_enemy_road())
                    new_enemy.pos = new_enemy.road.start_position
                    self.enemy_list.append(new_enemy)

    def iterate(self):
        if self.iteration_num % 4 == 0:
            for tower in self.tower_list:
                if tower.target is None:
                    tower.find_target(self.enemy_list)
                proj = tower.attack()
                if proj is None:
                    pass
                    #print("No Attack")
                else:
                    self.projectile_list.append(proj)

        if self.iteration_num % 2 == 0:
            delete_list = []
            for i in range(len(self.projectile_list)):
                proj = self.projectile_list[i]
                if proj.target not in self.enemy_list:
                    #print("Target lost: ", proj.target.pos)
                    #self.projectile_list.pop(i)
                    proj.source.target = None
                    delete_list.append(i)
                    continue
                if proj.move():
                    #print("Hit: ", proj.target.pos)
                    proj.target.hp -= proj.damage
                    #print(proj.target.hp, proj.damage)
                    delete_list.append(i)

                    proj.source.target = None
                    #self.projectile_list.pop(i)
                    continue

                #print("Proj pos: ", proj.position)
            for i in range(len(delete_list)-1, -1, -1):
                self.projectile_list.pop(delete_list[i])

        if self.iteration_num % 3 == 0 and self.delay <= self.iteration_num:
            for enemy in self.enemy_list:
                if enemy.hp <= 0:
                    #print("Killed")
                    self.enemy_killed+=1
                    self.enemy_list.remove(enemy)
                #print(self.map.get_random_enemy_road().road)
                elif not enemy.move():
                    #print(self.map.get_random_enemy_road().road)
                    #print(enemy.road.road)
                    self.enemy_passed += 1

                    self.enemy_list.remove(enemy)
                else:
                    pass
                    #print(enemy.pos, end=" ")
            #print()

        if self.iteration_num % 9 == 0 and self.delay <= self.iteration_num:
            new_enemy = self.enemy_generator.next_enemy()
            if new_enemy is None:
                if len(self.enemy_list) == 0:
                    pass
                    #print(self.enemy_list)
                    #print("End of Enemies")
                #print("End of Enemy list")
            else:
                new_enemy.road = copy.deepcopy(self.map.get_random_enemy_road())
                new_enemy.pos = new_enemy.road.start_position
                self.enemy_list.append(new_enemy)


        self.iteration_num += 1

