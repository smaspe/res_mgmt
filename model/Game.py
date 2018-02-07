import itertools
from collections import defaultdict
from typing import Iterable, DefaultDict, Mapping

from model.Building import Building, Blueprint
from model.Resource import Resource


class NotEnoughStockException(Exception):
    pass


class Game:
    def __init__(self):
        self.resources = None
        self.blueprints = None
        self.buildings = defaultdict(list)

    def build(self, blueprint: Blueprint):
        stocks = self.load()

        Game.withdraw(stocks, blueprint.build_cost)
        building = Building(blueprint)
        self.buildings[blueprint].append(building)

        self.unload(stocks)

    def all_buildings(self) -> Iterable[Building]:
        return itertools.chain(*self.buildings.values())

    def load(self) -> DefaultDict[Resource, int]:
        stocks = defaultdict(int)
        for building in self.all_buildings():
            building.load(stocks)
        return stocks

    def tick(self):
        stocks = self.load()
        # Created resources go in the new stock before going in the global stock
        new_stocks = defaultdict(int)
        for building in self.all_buildings():
            building.use(stocks, new_stocks)
        Game.deposit(stocks, new_stocks)
        self.unload(stocks)
        # Whatever is left in stocks is wasted

    def unload(self, stocks: DefaultDict[Resource, int]) -> None:
        for building in self.all_buildings():
            building.unload(stocks)

    # TODO refactor, not ideal to load everything every time
    def get_stock(self, resource: Resource) -> int:
        stocks = self.load()
        res = stocks[resource]
        self.unload(stocks)
        return res

    @staticmethod
    def withdraw(stocks: DefaultDict[Resource, int], costs: Mapping[Resource, int]):
        # Verify the costs
        for res, value in costs.items():
            if stocks[res] < value:
                raise NotEnoughStockException("Not enough " + res)
        # Apply the costs
        for res, value in costs.items():
            stocks[res] -= value

    @staticmethod
    def deposit(stocks: DefaultDict[Resource, int], gain: Mapping[Resource, int]):
        # Apply the gain
        for res, value in gain.items():
            stocks[res] += value
