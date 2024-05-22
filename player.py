class Player:

  def __init__(self):
      self.location = [0, 0]

  def change_location(self, x, y):
      self.location = [x, y]

  def get_location(self):
    return self.location