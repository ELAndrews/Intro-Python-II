# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, name, att):
        self.name = name
        self.att = att

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

        self.items = list()
        self.locked = False
        self.restricted = list()


class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
