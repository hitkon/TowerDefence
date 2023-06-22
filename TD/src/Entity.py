from Projectile import Projectile

class Entity:

    def __init__(self, hp, pos, projectile_info):
        self.hp = hp
        self.pos = pos
        self.projectile_info = projectile_info
        self.target = None

    def attack(self):
        if self.projectile_info is None or self.target is None:
            return None
        return Projectile(project_info=self.projectile_info, position=self.pos, target=self.target, source=self)

    def move(self):
        pass

    def getImage():
        pass

    def find_target(self, targets):
        if targets is None or len(targets) == 0:
            self.target = None
            return

        min_distance = self.pos.square_distance(targets[0].pos)
        cur_target = targets[0]
        for target in targets:
            if min_distance > self.pos.square_distance(target.pos):
                cur_target = target
                min_distance = self.pos.square_distance(target.pos)
        self.target = cur_target
