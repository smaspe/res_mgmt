class Storage:
    def __init__(self, game, resources):
        self.resource = {game.resource[k]: v for k, v in resources.items()}
