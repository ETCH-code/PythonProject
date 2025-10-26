class Player:
    def __init__ (self, x, y, size, color):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.speed = 5
    def move(self, x_dist, y_dist):
        self.x += x_dist
        self.y += y_dist

    player1.move(5, 2)