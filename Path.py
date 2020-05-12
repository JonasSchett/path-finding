class Path:
    def __init__(self, start_tile, end_tile):
        self.start = start_tile
        self.end = end_tile
        self.complete = False

        self.start.start = True
        self.end.end = True
        # using manhattan distance
        distance = self.end.position - self.start.position
        distance = abs(distance[0]) + abs(distance[1])
        self.start.estimated_cost = distance

        self.closed_list = []
        self.open_list = [self.start]

    def path_finding_part(self):
        if self.complete:
            return True

        if len(self.open_list) < 1:
            # done
            self.complete = True
            return True

        self.open_list = sorted(self.open_list, key=lambda tile: tile.get_score())
        best_tile = self.open_list.pop(0)

        if best_tile is self.end:
            # done
            best_tile.set_as_path()
            self.complete = True
            return True

        self.closed_list.append(best_tile)
        best_tile.closed = True
        grid = best_tile.grid
        for neighbour_location in best_tile.neighbours:
            neighbour = grid.get_tile(neighbour_location)
            if neighbour in self.closed_list or neighbour.walkable == False:
                pass
            elif neighbour in self.open_list:
                neighbour.update_movement_cost(best_tile)
            else:
                neighbour.set_movement_cost(best_tile)
                distance = self.end.position - neighbour.position
                distance = abs(distance[0]) + abs(distance[1])
                neighbour.estimated_cost = distance
                self.open_list.append(neighbour)
                neighbour.open = True
        return False

    def find_complete_path(self):
        while self.path_finding_part() is False:
            pass


