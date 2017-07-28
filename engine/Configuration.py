from model.Building import Blueprint
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
    Reads the capabilities from the relevant section of the config of a building's blueprint
    :param capabilities: the config section
    :param game: the context
    :return: a list of capabilities for that blueprint
    """
    return [CAPABILITIES[capa](game, conf) for capa, conf in capabilities.items()]


def read_blueprints(blueprints, game):
    for blueprint in blueprints:
        capabilities = read_capabilities(blueprint['capabilities'], game)
        building_cost = {game.resources[k]: v for k, v in blueprint['cost']}

        # TODO
        required_blueprints = []
        required_techs = []
        workers = {}

        yield Blueprint(blueprint['name'],
                        required_techs,
                        required_blueprints,
                        building_cost,
                        blueprint['time'],
                        capabilities,
                        workers,
                        blueprint['maximum'])


def read_config(config):
    """
    Creates a new blank game from the configuration
    :param config: a dict representing the config
    :return: a new game
    """
    game = Game()

    game.resources = read_resources(config['resources'])

    game.blueprints = list(read_blueprints(config['blueprints'], game))

    return game
