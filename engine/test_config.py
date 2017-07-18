from unittest import TestCase

import engine.Configuration as Configuration
from model.Game import Game
from model.Resource import Resource
from model.capabilities.Storage import Storage


class TestReadConfig(TestCase):
    def test_read_resources(self):
        config = ['wood', 'rock']
        res = Configuration.read_resources(config)
        self.assertTrue('wood' in res)
        self.assertTrue('rock' in res)
        self.assertEqual(res['rock'].res_id, 'rock')

    def test_read_capabilities(self):
        config = {'storage': {'wood': 10}}
        game = Game()
        game.resource = {'wood': Resource('wood')}
        res = Configuration.read_capabilities(config, game)
        self.assertTrue(res[0].__class__, Storage)

    def test_read_buildings(self):
        self.fail()
