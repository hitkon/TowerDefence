from Vector2d import Vector2d


class Projectile:

    def __init__(self, damage, speed, position, target, source):
        self.damage = damage
        self.speed = speed
        self.position = position
        self.target = target
        self.source = source

    def __init__(self, project_info, position, target, source):
        self.damage = project_info.damage
        self.speed = project_info.speed
        self.position = position
        self.target = target
        self.source = source

    def move(self):
        """change the position of projectile, return True if it reached the target, False otherwise"""
        dx = self.target.pos.x - self.position.x
        dy = self.target.pos.y - self.position.y
        if (dx ** 2 + dy ** 2) <= self.speed:
            self.target.hp -= self.damage
            return True
        t = (self.speed / (dx ** 2 + dy ** 2))
        self.position = Vector2d(self.position.x + t * dx, self.position.y + t * dy)
        return False


