from unittest import TestCase

from collections import defaultdict

from model.Resource import Resource
from model.capabilities.Production import Production


class TestProduction(TestCase):
    def test_produce_empty(self):
        stocks = defaultdict(int)
        wood = Resource('wood')
        beam = Resource('beam')
        production = Production({wood: 2}, {beam: 1}, None, None)
        production.use(stocks)
        self.assertEqual(0, stocks[beam])
        self.assertEqual(0, stocks[wood])

    def test_produce_not_enough(self):
        stocks = defaultdict(int)
        wood = Resource('wood')
        beam = Resource('beam')
        stocks[wood] = 1
        production = Production({wood: 2}, {beam: 1}, None, None)
        production.use(stocks)
        self.assertEqual(0, stocks[beam])
        self.assertEqual(1, stocks[wood])

    def test_produce(self):
        stocks = defaultdict(int)
        wood = Resource('wood')
        beam = Resource('beam')
        stocks[wood] = 3
        production = Production({wood: 2}, {beam: 1}, None, None)
        production.use(stocks)
        self.assertEqual(1, stocks[beam])
        self.assertEqual(1, stocks[wood])
