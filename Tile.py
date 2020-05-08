import numpy as np

class Tile:
    def __init__(self, grid, cost=1, position=(0, 0)):
        self.grid = grid

        self.cost = cost
        self.position = np.array(position)
        self.neighbours = [
            self.position + np.array((1, 0)),
            self.position + np.array((0, -1)),
            self.position + np.array((-1, 0)),
            self.position + np.array((0, 1)),
        ]
