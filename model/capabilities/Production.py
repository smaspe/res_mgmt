from model.Game import NotEnoughStockException, Game


class Production:
    def __init__(self, cost, gain, prod_time, workers):
        self.gain = gain
        self.cost = cost

    def load(self):
        pass

    def use(self, global_stock):
        try:
            Game.withdraw(global_stock, self.cost)
            Game.deposit(global_stock, self.gain)
        except NotEnoughStockException:
            # Excepted exception, as if there is not enough stock, just do nothing
            pass

    def unload(self, global_stock):
        pass
