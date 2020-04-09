

class Item:
    def __init__(self, name, descrition):
        self.name = name
        self.descrition = descrition


class Weapon(Item):
    def __init__(self, name, description, damage):
        self.damage = damage
        super().__init__(name, description)

    def __str__(self):
        print(f"\n {self.name} => {self.description} \n Damage: {self.damage} ")


class Tool(Item):
    def __init__(self, name, description):
        # self.size = size
        super().__init__(name, description)

    def __str__(self):
        print(f"\n {self.name} => {self.description}")


class Coins(Item):
    def __init__(self, name, description, amount):
        self.amount = amount
        super().__init__(name, description)

    def __str__(self):
        print(f"\n {self.amount} {self.name}")
