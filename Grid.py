import arcade
import random
from Path import Path
from Tile import Tile


class Grid(arcade.Window):
    def __init__(self, x_size=0, y_size=0, screen_x=600, screen_y=600, title="Awesome Path-finding", tile_size=20):
        super().__init__(screen_x, screen_y, title)
        self.x_size = x_size
        self.y_size = y_size
        self.tile_size = tile_size

        # just a list determining the relationship between walkable and not walkable tiles
        randomiser = [False, True, True, True]

        self.position_scaler = screen_x / x_size if x_size < y_size else screen_y / y_size

        self.x_offset = screen_x/2 - x_size / 2 * self.position_scaler + self.position_scaler / 2
        self.y_offset = screen_y/2 - y_size / 2 * self.position_scaler + self.position_scaler / 2
        self.tiles = [[Tile(self, position=(i, j), walkable=random.choice(randomiser)) for j in range(y_size)] for i in range(x_size)]
        self.path = None

        self.increment = 1
        self.increment_timer = 0
        arcade.set_background_color(arcade.color.BLACK_OLIVE)
        arcade.run()


    def on_draw(self):
        self.draw_tiles()

    def on_update(self, delta_time: float):
        if self.path is not None:
            for i in range(20):
                self.path.path_finding_part()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        self.create_random_path()

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

    def draw_tile(self, x, y, color, size=20.0):
        arcade.draw_point(x * self.position_scaler + self.x_offset,
                          y * self.position_scaler + self.y_offset,
                          color, size)
    def draw_tiles(self):
        arcade.start_render()
        for column in self.tiles:
            for tile in column:
                (x, y) = tile.position
                if not tile.walkable:
                    self.draw_tile(x, y, arcade.color.DARK_BROWN, self.tile_size)
                elif tile.start:
                    self.draw_tile(x,y,arcade.color.YELLOW_ORANGE, self.tile_size*1.2)
                elif tile.end:
                    self.draw_tile(x,y,arcade.color.BRIGHT_LILAC, self.tile_size*1.2)
                elif tile.part_of_path:
                    self.draw_tile(x,y,arcade.color.RED, self.tile_size)
                elif tile.closed:
                    self.draw_tile(x,y,arcade.color.DARK_GREEN, self.tile_size)
                elif tile.open:
                    self.draw_tile(x,y,arcade.color.DARK_BLUE, self.tile_size)
                else:
                    self.draw_tile(x,y,arcade.color.GREEN, self.tile_size)
    def get_tile(self, position):
        # loop over edges of map with mod operator
        return self.tiles[position[0] % self.x_size][position[1] % self.y_size]
