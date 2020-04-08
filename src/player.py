# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, curr_room):
        self.name = name
        self.curr_room = curr_room

    def __str__(self):
        return (f'Welcome {self.name}! You have arrived {self.curr_room.name}. Time for your adventure to begin...')
