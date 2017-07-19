from model.Game import NotEnoughStockException


class Production:
    def __init__(self, cost, gain, prod_time, workers):
        self.gain = gain
        self.cost = cost

    def apply(self, game):
        try:
            game.withdraw(self.cost)
            game.deposit(self.gain)
        except NotEnoughStockException:
            # Excepted exception, as if there is not enough stock, just do nothing
            pass
