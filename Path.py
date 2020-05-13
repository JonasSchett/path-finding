class Path:
    """Path class creating a path from the start to end"""
    def __init__(self, start_tile, end_tile):
        self.start = start_tile
        self.end = end_tile

        # variable storing if this path is complete
        self.complete = False

        # setting tile parameters for visualisation
        self.start.start = True
        self.end.end = True

        # using manhattan distance for distance between tiles
        distance = self.end.position - self.start.position
        distance = abs(distance[0]) + abs(distance[1])
        self.start.estimated_cost = distance

        # closed and open list for A* path finding are
        # initialised with just the start tile
        self.closed_list = []
        self.open_list = [self.start]

    def path_finding_step(self):
        if self.complete:
            return True

        # if the open list is empty, we are done, but have not found a solution
        if len(self.open_list) < 1:
            self.complete = True
            return True

        # Sort the open list to retrieve the best item
        self.open_list = sorted(self.open_list, key=lambda tile: tile.get_score())
        best_tile = self.open_list.pop(0)

        # if we have reached the end, we are done and found a solution
        # We now have the whole path
        if best_tile is self.end:
            best_tile.set_as_path()
            self.complete = True
            return True

        # calculations are performed for best tile and it is also closed and done
        self.closed_list.append(best_tile)
        best_tile.closed = True
        grid = best_tile.grid
        # calculations are done for all neighbours of the tile
        for neighbour_location in best_tile.neighbours:
            neighbour = grid.get_tile(neighbour_location)
            # if the neighbour is already closed, we ignore it
            if neighbour in self.closed_list or neighbour.walkable == False:
                pass
            elif neighbour in self.open_list:
                # values are updated for the neighbour, this includes recalculation of the tile costs
                neighbour.update_cost(best_tile)
            else:
                # values are calculated for the first time for this neighbour
                neighbour.set_initial_cost(best_tile, self.end.position)

                self.open_list.append(neighbour)
                neighbour.open = True
        return False

    def find_complete_path(self):
        # function simply executing find path until it's done
        while self.path_finding_step() is False:
            pass


