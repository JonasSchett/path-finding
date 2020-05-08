import arcade
from Tile import Tile


class Grid(arcade.Window):
    def __init__(self, x_size=0, y_size=0, screen_x=600, screen_y=600, title="Awesome Path-finding", draw_scaler = 20):
        super().__init__(screen_x, screen_y, title)
        self.x_size = x_size
        self.y_size = y_size
        self.draw_scaler = draw_scaler
        self.x_offset = screen_x/2 - self.draw_scaler * self.x_size/2
        self.y_offset = screen_y/2 - self.draw_scaler * self.y_size/2
        self.tiles = [[Tile(self, position=(i, j)) for j in range(y_size)] for i in range(x_size)]
        arcade.run()

    def on_draw(self):
        arcade.start_render()
        for column in self.tiles:
            for tile in column:
                (x, y) = tile.position
                arcade.draw_point(x*self.draw_scaler + self.x_offset,
                                  y*self.draw_scaler + self.y_offset,
                                  arcade.color.DARK_CYAN, 30)

    def on_update(self, delta_time: float):
        pass


    def getTile(self, position):
        return self.tiles[position[0]][position[1]]
