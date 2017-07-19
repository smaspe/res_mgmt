from collections import defaultdict

from model.Building import Building


class NotEnoughStockException(Exception):
    pass


class Game:
    def __init__(self):
        self.resources = None
        self.blueprints = None
        self.buildings = defaultdict(list)
        self.stocks = defaultdict(int)

    def withdraw(self, costs):
        # Verify the costs
        for res, value in costs.items():
            if self.stocks[res] < value:
                raise NotEnoughStockException("Not enough " + res.res_id)
        # Apply the costs
        for res, value in costs.items():
            self.stocks[res] -= value

    def deposit(self, gain):
        # Apply the gain
        # TODO check storage capability
        for res, value in gain.items():
            self.stocks[res] += value

    def build(self, blueprint):
        self.withdraw(blueprint.build_cost)
        building = Building(blueprint.capabilities)
        self.buildings[blueprint].append(building)

    def tick(self):
        for building_list in self.buildings:
            for building in building_list:
                building.apply_capabilities(self)

