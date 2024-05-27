class Map:

    def __init__(self):
        self.world_map = self.get_world_map("map.txt")

    def get_world_map(self, map_file):
        world_map = {}
        try:
            with open(map_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(": ", 1)
                    if len(parts) == 2:
                        position, description = parts
                        if position:
                            try:
                                position_tuple = tuple(
                                    int(x) for x in parts[0].split(', '))
                                world_map[position_tuple] = description
                            except ValueError:
                                print(
                                    f"Issue converting position to integer for description: {description}"
                                )
                    else:
                        print(f"Invalid entry in map file: {line}")
        except FileNotFoundError:
            print(f"Error opening map file: {map_file}")
        except PermissionError:
            print(f"Insufficient permissions to read map file: {map_file}")
        return world_map

    def get_map(self):
        return self.world_map

    def get_formatted_map(self):
        """
        Generates a textual representation of the world map with room descriptions.
        """
        max_x, max_y = self.get_map_dimensions()
        map_rows = []
        for y in range(max_y + 1):
            row = []
            for x in range(max_x + 1):
                room_description = self.world_map.get((x, y), "???")
                row.append(
                    f"{room_description:<20}")  # Pad with spaces for alignment
            map_rows.append(" ".join(row))
        return "\n".join(map_rows)

    # ... (existing methods)

    def get_map_dimensions(self):
        """
        Returns the maximum X and Y coordinates of the world map.
        """
        max_x = max([key[0] for key in self.world_map.keys()])
        max_y = max([key[1] for key in self.world_map.keys()])
        return max_x, max_y

    def get_formatted_map(self):
        """
        Generates a textual representation of the world map with room descriptions.
        """
        max_x, max_y = self.get_map_dimensions()
        map_rows = []
        for y in range(max_y + 1):
            row = []
            for x in range(max_x + 1):
                room_description = self.world_map.get((x, y), "???")
                row.append(
                    f"{room_description:<20}")  # Pad with spaces for alignment
            map_rows.append(" ".join(row))
        return "\n".join(map_rows)
