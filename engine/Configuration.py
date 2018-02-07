from typing import Mapping, Iterable, List, Any

from model.Building import Blueprint
from model.Game import Game
from model.Resource import Resource
from model.capabilities.Production import Production
from model.capabilities.Storage import Storage

CAPABILITIES = {'storage': Storage, 'production': Production}


def read_resources(resources: Iterable[str]) -> Mapping[str, Resource]:
    """
    Reads the resources from the relevant section of the config
    :param resources: the config section
    :return: a dict of resources
    """
    return {k: Resource(k) for k in resources}


def read_capabilities(capabilities) -> Mapping[str, List[Any]]:
    """
    Reads the capabilities from the relevant section of the config of a building's blueprint
    :param capabilities: the config section
    :return: a mapping of capabilities for that blueprint
    """
    return {capa: [CAPABILITIES[capa](**conf) for conf in confs] for capa, confs in capabilities.items()}


def read_blueprints(blueprints) -> Iterable[Blueprint]:
    for blueprint in blueprints:
        capabilities = read_capabilities(blueprint['capabilities'])

        # TODO
        required_blueprints = []
        required_techs = []
        workers = {}

        yield Blueprint(blueprint['name'],
                        required_techs,
                        required_blueprints,
                        blueprint['cost'],
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

    game.blueprints = list(read_blueprints(config['blueprints']))

    return game
