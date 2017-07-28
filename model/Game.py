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
        stocks = self.load()

        Game.withdraw(stocks, blueprint.build_cost)
        building = Building(blueprint)
        self.buildings[blueprint].append(building)

        self.unload(stocks)

    def load(self):
        stocks = defaultdict(int)
        for capability in self.iter_capabilities():
            capability.load(stocks)
        return stocks

    def iter_capabilities(self):
        for building_list in self.buildings.values():
            for building in building_list:
                for capability in building.capabilities:
                    yield capability

    def tick(self):
        stocks = self.load()
        for capability in self.iter_capabilities():
            capability.use(stocks)
        self.unload(stocks)
        # Whatever is left in stocks is wasted

    def unload(self, stocks):
        for capability in self.iter_capabilities():
            capability.unload(stocks)

    # TODO refactor, not ideal to load everything every time
    def get_stock(self, resource):
        stocks = self.load()
        res = stocks[resource]
        self.unload(stocks)
        return res

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
