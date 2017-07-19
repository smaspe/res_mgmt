class Blueprint:
    def __init__(self, req_tech, req_blueprint, build_cost, build_time, capabilities, workers, max_instances=-1):
        self.capabilities = capabilities
        self.build_cost = build_cost


class Building:
    def __init__(self, capabilities):
        self.capabilities = capabilities

    def apply_capabilities(self, game):
        for capability in self.capabilities:
            capability.apply(game)
