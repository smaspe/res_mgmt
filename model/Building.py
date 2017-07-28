class Blueprint:
    def __init__(self, name, req_tech, req_blueprint, build_cost, build_time, capabilities, workers, max_instances=-1):
        self.name = name
        self.capabilities = capabilities
        self.build_cost = build_cost

    def __str__(self):
        return self.name


class Building:
    def __init__(self, capabilities):
        self.capabilities = capabilities

    def apply_capabilities(self, game):
        for capability in self.capabilities:
            capability.apply(game)
