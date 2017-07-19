class Blueprint:
    def __init__(self, req_tech, req_blueprint, build_cost, build_time, capabilities, workers, max_instances=-1):
        self.build_cost = build_cost

    def build(self, game):
        game.withdraw(self.build_cost)
        return Building()


class Building:
    def __init__(self):
        pass
