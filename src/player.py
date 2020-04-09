# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item


class Player:
    def __init__(self, name, curr_room):
        self.name = name
        self.curr_room = curr_room
        self.inventory = []
        self.gold = 0

    def __str__(self):
        return (f'Welcome {self.name}! You have arrived {self.curr_room.name}. Time for your adventure to begin...')

    # def pick_up(self, item):

    # def drop_item(self, item)
