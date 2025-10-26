class Player:
    def __init__ (self, name, health, max_health, attack, inventory):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.inventory = inventory

    def damage(self, d):
        self.health = max(self.health - d, 0)

    def consume(self, h, a):
        self.health = min(self.health + h, self.max_health)
        self.attack += a

    def collect(self, item):
        self.inventory.append(item)