class Player:

    def __init__(self):
        self.x = 0
        self.y = 0

    def get_location(self):
        return self.x, self.y

    def set_location(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
