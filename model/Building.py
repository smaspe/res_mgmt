from copy import deepcopy
from typing import Mapping, DefaultDict

from model.Resource import Resource


class Blueprint:
    def __init__(self, name, req_tech, req_blueprint, build_cost: DefaultDict[Resource, int], build_time,
                 capabilities: Mapping, workers, max_instances=-1):
        self.name = name
        self.capabilities = capabilities
        self.build_cost = build_cost

    def __str__(self):
        return self.name


class Building:
    def __init__(self, blueprint: Blueprint):
        self.name = blueprint.name
        self.capabilities = deepcopy(blueprint.capabilities)

    def load(self, global_stock: DefaultDict[Resource, int]) -> None:
        for capability in self.capabilities['storage']:
            capability.load(global_stock)

    def unload(self, global_stock) -> None:
        for capability in self.capabilities['storage']:
            capability.unload(global_stock)

    def use(self, global_stock: DefaultDict[Resource, int], new_stock: DefaultDict[Resource, int]) -> None:
        for capability in self.capabilities['production']:
            capability.use(global_stock, new_stock)
