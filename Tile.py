import numpy as np

class Tile:
    def __init__(self, grid, cost=1, position=(0, 0), walkable=True):
        self.grid = grid
        self.cost = cost
        self.parent = None

        self.start = False
        self.part_of_path = False
        self.end = False
        self.closed = False
        self.open = False


        self.movement_cost = 0
        self.estimated_cost = 0
        self.total_score = self.movement_cost + self.estimated_cost
        self.walkable = walkable
        self.position = np.array(position)

        self.neighbours = [
            self.position + np.array((1, 0)),
            self.position + np.array((0, -1)),
            self.position + np.array((-1, 0)),
            self.position + np.array((0, 1)),
        ]

    def set_as_path(self):
        self.part_of_path = True

        if self.parent is not None:
            self.parent.set_as_path()

    def clear_path(self):
        self.parent = None
        self.start = False
        self.part_of_path = False
        self.end = False
        self.closed = False
        self.open = False

    def get_score(self):
        return self.estimated_cost + self.movement_cost

    def set_movement_cost(self, best_tile):
        self.movement_cost = self.cost + best_tile.movement_cost
        self.total_score = self.movement_cost + self.estimated_cost
        self.parent = best_tile

    def update_movement_cost(self, best_tile):
        if (self.cost + best_tile.movement_cost + self.estimated_cost) < self.total_score:
            self.movement_cost = self.cost + best_tile.movement_cost
            self.total_score = self.movement_cost + self.estimated_cost
            self.parent = best_tile
        self.total_score = self.movement_cost + self.estimated_cost

