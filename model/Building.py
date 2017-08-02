from copy import deepcopy


class Blueprint:
    def __init__(self, name, req_tech, req_blueprint, build_cost, build_time, capabilities, workers, max_instances=-1):
        self.name = name
        self.capabilities = capabilities
        self.build_cost = build_cost

    def __str__(self):
        return self.name


class Building:
    def __init__(self, blueprint):
        self.name = blueprint.name
        self.capabilities = deepcopy(blueprint.capabilities)

    def load(self, global_stock):
        for capability in self.capabilities['storage']:
            capability.load(global_stock)

    def unload(self, global_stock):
        for capability in self.capabilities['storage']:
            capability.unload(global_stock)

    def use(self, global_stock):
        for capability in self.capabilities['production']:
            capability.use(global_stock)
