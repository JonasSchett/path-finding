import random
from Path import Path
from Tile import Tile


class Grid:
    """Grid class simply storing the grid with tiles"""
    def __init__(self, x_size=0, y_size=0, walkable_rate=0.75):

        self.x_size = x_size
        self.y_size = y_size

        # tiles are initialised and are either walkable or not depending on a random number comparison
        # with the walkable_rate (0.75 means 75% of tiles are walkable)
        self.tiles = [[Tile(self, position=(i, j), walkable=(random.random() < walkable_rate))
                       for j in range(y_size)] for i in range(x_size)]

        # Path no initialised at start
        self.path = None

    def create_random_path(self):
        # function creating a random path
        for column in self.tiles:
            for tile in column:
                tile.clear_tile()

        walkable_tiles = []
        for column in self.tiles:
            for tile in column:
                if tile.walkable:
                    walkable_tiles.append(tile)

        start = random.choice(walkable_tiles)
        end = random.choice(walkable_tiles)
        self.path = Path(start, end)

    def get_tile(self, position):
        # loop over edges of map with mod operator
        return self.tiles[position[0] % self.x_size][position[1] % self.y_size]
