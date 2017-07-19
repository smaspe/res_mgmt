from collections import defaultdict


class NotEnoughStockException(Exception):
    pass


class Game:
    def __init__(self):
        self.resources = None
        self.blueprints = None
        self.stocks = defaultdict(int)

    def withdraw(self, costs):
        # Verify the costs
        for res, value in costs.items():
            if self.stocks[res] < value:
                raise NotEnoughStockException("Not enough " + res.res_id)
        # Apply the costs
        for res, value in costs.items():
            self.stocks[res] -= value

    def tick(self):
        pass
