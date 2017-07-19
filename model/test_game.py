from unittest import TestCase

from model.Game import Game, NotEnoughStockException
from model.Resource import Resource


class TestGame(TestCase):
    def test_withdraw_empty_from_empty(self):
        game = Game()
        game.withdraw({})

    def test_withdraw_from_empty(self):
        wood = Resource('wood')
        game = Game()
        try:
            game.withdraw({wood: 10})
            self.fail('Should throw an exception')
        except NotEnoughStockException:
            pass

    def test_withdraw(self):
        wood = Resource('wood')
        game = Game()
        game.stocks[wood] = 100
        game.withdraw({wood: 10})
        self.assertEqual(90, game.stocks[wood])

    def test_tick(self):
        pass
