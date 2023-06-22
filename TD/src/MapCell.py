import pygame

class MapCell:

    types = {0: "EMPTY", 1: "ROAD", 2: "IN", 3: "OUT"}

    def __init__(self, pos, cell_type: types):
        self.pos = pos
        self.cell_type = cell_type
        self.entity = None

    def getImage(self):
        image = None
        if self.cell_type == 0:
            image = pygame.image.load("images/grass.jpg")
            image = pygame.transform.scale(image, (50, 50))
        elif self.cell_type == 1:
            image = pygame.image.load("images/road.jpg")
            image = pygame.transform.scale(image, (50, 50))
        else :
            image = pygame.image.load("images/portal.png").convert_alpha()
            image = pygame.transform.scale(image, (50, 50))
            image.set_colorkey()
            #image.set_alpha(128)
        return image

    def __str__(self):
        return "(" + str(self.pos.x) + "," + str(self.pos.y) + "):" + self.types[self.cell_type]

    def add_entity(self, entity):
        self.entity = entity

    def remove_entity(self):
        self.entity = None