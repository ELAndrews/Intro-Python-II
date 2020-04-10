

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)


class Tool(Item):
    def __init__(self, name, description):
        # self.size = size
        super().__init__(name, description)


class Coins(Item):
    def __init__(self, name, description, amount):
        self.amount = amount
        super().__init__(name, description)
