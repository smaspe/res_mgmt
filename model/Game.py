from collections import defaultdict

from model.Building import Building


class NotEnoughStockException(Exception):
    pass


class Game:
    def __init__(self):
        self.resources = None
        self.blueprints = None
        self.buildings = defaultdict(list)

    def build(self, blueprint):
        stocks = defaultdict(int)
        for capability in self.iter_capabilities():
            capability.load(stocks)

        Game.withdraw(stocks, blueprint.build_cost)
        building = Building(blueprint.capabilities)
        self.buildings[blueprint].append(building)

        for capability in self.iter_capabilities():
            capability.unload(stocks)

    def iter_capabilities(self):
        for building_list in self.buildings:
            for building in building_list:
                for capability in building.capabilities:
                    yield capability

    def tick(self):
        stocks = defaultdict(int)
        for capability in self.iter_capabilities():
            capability.load(stocks)
        for capability in self.iter_capabilities():
            capability.use(stocks)
        for capability in self.iter_capabilities():
            capability.unload(stocks)

    @staticmethod
    def withdraw(stocks, costs):
        # Verify the costs
        for res, value in costs.items():
            if stocks[res] < value:
                raise NotEnoughStockException("Not enough " + res.res_id)
        # Apply the costs
        for res, value in costs.items():
            stocks[res] -= value

    @staticmethod
    def deposit(stocks, gain):
        # Apply the gain
        for res, value in gain.items():
            stocks[res] += value
