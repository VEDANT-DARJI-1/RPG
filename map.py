class Map:
  def __init__(self):
      self.world_map = {}
  def get_location_description(self, x, y):
      return self.world_map.get((x, y), "Unknown room")

