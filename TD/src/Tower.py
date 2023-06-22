from Entity import Entity


class Tower(Entity):
    cost = 0

    def __init__(self, attack_speed, attack_range, build_time, pos, proj_info):
        super().__init__(0, pos, proj_info)
        self.attack_speed = attack_speed
        self.attack_range = attack_range
        self.build_time = build_time
        #print("Tower __init")









