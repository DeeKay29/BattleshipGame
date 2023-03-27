class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coords = []
        self.is_sunk = False