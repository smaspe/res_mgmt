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
        self.assertEqual(res['rock'], 'rock')

    def test_read_capabilities(self):
        game = Game()
        game.resources = {'wood': Resource('wood')}
        config = {'storage': [{'wood': 10}]}
        res = Configuration.read_capabilities(config)
        self.assertTrue(res['storage'][0].__class__, Storage)

    def test_read_blueprints(self):
        game = Game()
        config = [{'name': 'Test Blueprint', 'capabilities': {}, 'cost': {}, 'time': 10, 'maximum': 1}]
        res = list(Configuration.read_blueprints(config))
        self.assertEqual(1, len(res))
