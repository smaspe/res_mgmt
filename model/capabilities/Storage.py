class Storage:
    def __init__(self, game, resources):
        self.capacity = {game.resource[k]: v for k, v in resources.items()}
        self.stock = {}

    def load(self, global_stock):
        for key in set(global_stock.keys() + self.stock.keys()):
            global_stock[key] = global_stock[key] + self.stock.get(key, 0)

    def use(self, global_stock):
        pass

    def unload(self, global_stock):
        self.stock = {}
        for resource, capa in self.capacity.items():
            val = min(capa - self.stock[resource], global_stock[resource])
            self.stock[resource] -= val
            global_stock[resource] -= val
