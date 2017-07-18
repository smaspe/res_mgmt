from model.Building import Building
from model.Game import Game
from model.Resource import Resource
from model.capabilities.Storage import Storage

CAPABILITIES = {'storage': Storage}


def read_resources(resources):
    """
    Reads the resources from the relevant section of the config
    :param resources: the config section
    :return: a dict of resources
    """
    return {k: Resource(k) for k in resources}


def read_capabilities(capabilities, game):
    """
    Reads the capabilities from the relevant section of the config of a building
    :param capabilities: the config section
    :param game: the context
    :return: a list of capabilities for that building
    """
    return [CAPABILITIES[capa](game, conf) for capa, conf in capabilities.items()]


def read_buildings(buildings, game):
    for building in buildings:
        capabilities = read_capabilities(building['capabilities'], game)
        building_cost = {game.resources[k]: v for k, v in building['cost']}

        # TODO
        required_building = []
        required_techs = []
        workers = {}

        yield Building(required_techs,
                       required_building,
                       building_cost,
                       building['time'],
                       capabilities,
                       workers,
                       building['maximum'])


def read_config(config):
    """
    Creates a new blank game from the configuration
    :param config: a dict representing the config
    :return: a new game
    """
    game = Game()

    game.resources = read_resources(config['resources'])

    game.buildings = list(read_buildings(config['buildings'], game))

    return game
