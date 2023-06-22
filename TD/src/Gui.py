import pygame
from Engine import Engine
from Map import Map
from ArrowTower import ArrowTower
from Vector2d import Vector2d
from ProjectileInfo import ProjectileInfo
from CanonTower import CanonTower

class Gui:



    def __init__(self):
        # gui params init

        cell_size = 50
        clock = pygame.time.Clock()

        pygame.init()

        game_map = Map("maps/map1.txt")
        game_eng = Engine(game_map)

        # map initialization
        map_h, map_w = game_map.height, game_map.width
        size = width, height = cell_size * (map_w + 1), cell_size*(map_h+1)
        tower_clicked = -1

        myfont = pygame.font.SysFont("monospace", 15)

        # arrow = pygame.image.load("images/arrow.jpg")
        # arrow = pygame.transform.scale(arrow, (25, 25))
        arr_tower = pygame.image.load("images/ArrowTower.jpg")
        arr_tower = pygame.transform.scale(arr_tower, (50, 50))
        can_tower = pygame.image.load("images/canon.png")
        can_tower = pygame.transform.scale(can_tower, (50, 50))

        screen = pygame.display.set_mode(size)

        def is_tower_clicked(event):
            return (
                    map_w * cell_size <= event.pos[0] <= width and
                    0 <= event.pos[1] <= 2*cell_size
            )

        # main loop
        while True:
            screen.fill((255, 255, 255))
            clock.tick(15)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    #print(event.pos[0], event.pos[1])
                    if event.button == 1 and is_tower_clicked(event):

                        tower_clicked = event.pos[1] // cell_size
                        print(tower_clicked)

                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1 and tower_clicked != -1:

                        x = int(event.pos[0] / cell_size)
                        y = int(event.pos[1] / cell_size)

                        if map_w > y >= 0 and 0 <= x < map_h and 0 == game_map.field[y][x].cell_type  \
                                and not game_map.is_occupied(Vector2d(y,x)):
                            #print(event.pos[0], event.pos[1], y, x)
                            if tower_clicked == 0:
                                game_eng.addTower(ArrowTower(Vector2d(y, x), 0, ProjectileInfo(1, 3, "images/arrow.jpg")))
                            elif tower_clicked == 1:
                                game_eng.addTower(CanonTower(Vector2d(y, x), 0, ProjectileInfo(0.5, 7, "images/canon_proj.png")))

                        tower_clicked = -1
                if event.type == pygame.MOUSEMOTION:
                    pass

            screen.blit(arr_tower, (map_w * cell_size, 0 * cell_size))
            screen.blit(can_tower, (map_w * cell_size, 1 * cell_size))

            # map drawing
            for i in range(map_w):
                for j in range(map_h):
                    screen.blit(game_map.field[i][j].getImage(), (j * cell_size, i * cell_size))


            for enemy in game_eng.enemy_list:
                screen.blit(enemy.getImage(), (enemy.pos.y * cell_size, enemy.pos.x * cell_size))

            for tower in game_eng.tower_list:
                screen.blit(tower.getImage(), (tower.pos.y * cell_size, tower.pos.x * cell_size))

            for proj in game_eng.projectile_list:
                screen.blit(proj.getImage(), (proj.position.y * cell_size, proj.position.x * cell_size))


            if tower_clicked != -1:
                #print(event.pos[0], event.pos[1])
                if tower_clicked == 0:
                    screen.blit(arr_tower, (event.pos[0], event.pos[1]))
                elif tower_clicked == 1:
                    screen.blit(can_tower, (event.pos[0], event.pos[1]))

            #pygame.display.flip()

            label = myfont.render("Killed: " + str(game_eng.enemy_killed), 1, (0, 0, 0))
            label2 = myfont.render("Passed: " + str(game_eng.enemy_passed), 1, (0, 0, 0))
            screen.blit(label, (36,419))
            screen.blit(label2, (170, 419))

            pygame.display.update()
            game_eng.iterate()

