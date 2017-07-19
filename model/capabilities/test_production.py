from unittest import TestCase

from model.Game import Game
from model.Resource import Resource
from model.capabilities.Production import Production


class TestProduction(TestCase):
    def test_produce_empty(self):
        game = Game()
        wood = Resource('wood')
        beam = Resource('beam')
        production = Production({wood: 2}, {beam: 1}, None, None)
        production.apply(game)
        self.assertEqual(0, game.stocks[beam])
        self.assertEqual(0, game.stocks[wood])

    def test_produce_not_enough(self):
        game = Game()
        wood = Resource('wood')
        beam = Resource('beam')
        game.stocks[wood] = 1
        production = Production({wood: 2}, {beam: 1}, None, None)
        production.apply(game)
        self.assertEqual(0, game.stocks[beam])
        self.assertEqual(1, game.stocks[wood])

    def test_produce(self):
        game = Game()
        wood = Resource('wood')
        beam = Resource('beam')
        game.stocks[wood] = 3
        production = Production({wood: 2}, {beam: 1}, None, None)
        production.apply(game)
        self.assertEqual(1, game.stocks[beam])
        self.assertEqual(1, game.stocks[wood])
