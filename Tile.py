import numpy as np

class Tile:
    """Tile storing data of a single tile and details of how to reach neighbours"""
    def __init__(self, grid, cost=1, position=(0, 0), walkable=True):
        # Grid the tile is part of
        self.grid = grid
        self.cost = cost
        self.parent = None

        # stored information about the tile used for visualisation
        self.start = False
        self.part_of_path = False
        self.end = False
        self.closed = False
        self.open = False

        # Costs used for pathfinding
        self.movement_cost = 0
        self.estimated_cost = 0
        self.total_score = self.movement_cost + self.estimated_cost

        # details if this tile is walkable or not
        self.walkable = walkable
        self.position = np.array(position)

        self.neighbours = [
            self.position + np.array((1, 0)),
            self.position + np.array((0, -1)),
            self.position + np.array((-1, 0)),
            self.position + np.array((0, 1)),
        ]

    # defines this tile as part of a path, used for visualisation
    def set_as_path(self):
        self.part_of_path = True

        if self.parent is not None:
            self.parent.set_as_path()

    # cleares the visualisation values of the tile
    def clear_tile(self):
        self.parent = None
        self.start = False
        self.part_of_path = False
        self.end = False
        self.closed = False
        self.open = False

    def get_score(self):
        return self.estimated_cost + self.movement_cost

    # movement cost is calculated initially and
    def set_initial_cost(self, best_tile, target_position):
        # we initially calculate the distance to the target position
        distance = target_position - self.position
        distance = abs(distance[0]) + abs(distance[1])
        self.estimated_cost = distance

        # then we set the best tile to the first tile we got
        self.set_best_tile(best_tile)


    def update_cost(self, best_tile):
        # we reset the best tile if the cost is better
        if (self.cost + best_tile.movement_cost + self.estimated_cost) < self.total_score:
            self.set_best_tile(best_tile)

    def set_best_tile(self, best_tile):
        self.movement_cost = self.cost + best_tile.movement_cost
        self.total_score = self.movement_cost + self.estimated_cost
        self.parent = best_tile

