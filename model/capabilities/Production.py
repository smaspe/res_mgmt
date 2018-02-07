from typing import DefaultDict

from model.Game import NotEnoughStockException, Game
from model.Resource import Resource


class Production:
    def __init__(self, cost: DefaultDict[Resource, int], gain: DefaultDict[Resource, int], prod_time, workers):
        self.cost = cost
        self.gain = gain

    def use(self, global_stock: DefaultDict[Resource, int], new_stock: DefaultDict[Resource, int]):
        try:
            Game.withdraw(global_stock, self.cost)
            Game.deposit(new_stock, self.gain)
        except NotEnoughStockException:
            # Expected exception, as if there is not enough stock, just do nothing
            pass
