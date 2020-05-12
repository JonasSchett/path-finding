import arcade
import random
from Path import Path
from Tile import Tile


class Grid():
    def __init__(self, x_size=0, y_size=0):

        self.x_size = x_size
        self.y_size = y_size

        # just a list determining the relationship between walkable and not walkable tiles
        randomiser = [False, True, True, True]
        self.tiles = [[Tile(self, position=(i, j), walkable=random.choice(randomiser)) for j in range(y_size)] for i in range(x_size)]
        self.path = None

    def create_random_path(self):
        for column in self.tiles:
            for tile in column:
                tile.clear_path()

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
