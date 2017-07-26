from unittest import TestCase

from collections import defaultdict

from model.Game import Game, NotEnoughStockException
from model.Resource import Resource


class TestGame(TestCase):
    def test_withdraw_empty_from_empty(self):
        Game.withdraw(defaultdict(), {})

    def test_withdraw_from_empty(self):
        wood = Resource('wood')
        try:
            Game.withdraw(defaultdict(int), {wood: 10})
            self.fail('Should throw an exception')
        except NotEnoughStockException:
            pass

    def test_withdraw(self):
        wood = Resource('wood')
        stocks = defaultdict(int)
        stocks[wood] = 100
        Game.withdraw(stocks, {wood: 10})
        self.assertEqual(90, stocks[wood])

    def test_tick(self):
        pass
