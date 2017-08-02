from model.Game import NotEnoughStockException, Game


class Production:
    def __init__(self, game, cost, gain, prod_time, workers):
        self.cost = cost
        self.gain = gain

    def use(self, global_stock):
        try:
            Game.withdraw(global_stock, self.cost)
            Game.deposit(global_stock, self.gain)
        except NotEnoughStockException:
            # Expected exception, as if there is not enough stock, just do nothing
            pass
