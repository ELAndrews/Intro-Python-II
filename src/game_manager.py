from room import Room, Riddle
from player import Player
from item import Item, Tool, Weapon, Coins

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, west and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
    Sadly, it has already been completely emptied by earlier adventurers. 
    The only exit is to the south."""),

    'gatekeep':  Room("The Gate Keep",
                      "The Gate Keeper stands before the dungeon enternce. To pass you must answer his riddle to enter."),

    'hall':  Room("The Great Hall",
                  """The hall is barely lite, on a flicker of an rusting oil lamp gaurded by fresh skeleton... 
    rotting flesh fills the air. 
    A passages run Noirth and South"""),

    'armoury':  Room("The Armoury",
                     """The walls are laden with shields, swords, axes... or so they should be, given the empty hooks and rakes.
    A glimmer of hope when the Great Hall light is reflected by something half hidden.
    The only exit is North."""),

    'dungeon':  Room("The Dungeon",
                     """3 prison cells, one to the north, the east and the West; the Great Hall to the South. 
    Blood curding screams pierce your ears in the West prison; its door barricade.
    Silence rings from the other 2 locked cells."""),

    'northCell':  Room("The North Cell",
                       """The sun blinds you suddenly... you smell salt and it burns your nose. 
    Your eyes adjust and you see an empty room with a sudden drop off to the clift."""),

    'eastCell':  Room("The East Cell",
                      """The smell of rotting flesh is putrid. 
    A decomposing corpse lies in a puddle of its own coagulated blood.
    Scratch marks coat the walls
    he corpse holds a rusty knife with a jagged."""),

}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['gatekeep']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['gatekeep'].e_to = room['foyer']
room['gatekeep'].w_to = room['hall']
room['hall'].e_to = room['foyer']
room['hall'].s_to = room['armoury']
room['armoury'].n_to = room['hall']
room['hall'].n_to = room['dungeon']
room['dungeon'].s_to = room['hall']
room['dungeon'].n_to = room['northCell']
room['northCell'].s_to = room['dungeon']
room['dungeon'].e_to = room['eastCell']
room['eastCell'].w_to = room['dungeon']


# Link rooms to Items

room['overlook'].items.append(Tool(
    "Cloak", "A travelers cloak made of silk with a cotton lining"))
room['overlook'].items.append(Coins("Gold Coins", "Gold Coins", 4))
room['treasure'].items.append(Coins("Gold Coins", "2 Rusty Old Gold Coins", 2))
room['armoury'].items.append(
    Weapon("Sword", "A beautiful Flamberge. a two-handed, wavy blade sword.", 5))
room['dungeon'].items.append(
    Tool("Skeleton Key", "Small, unassuming, master key."))
room['eastCell'].items.append(
    Weapon("Rusty Knife", "A small rusty and corroding knife", 1))


# Room restrictions

room['treasure'].locked = True
room['eastCell'].locked = True
room['northCell'].locked = True
room['gatekeep'].locked = True

room['treasure'].restricted.append("Skeleton Key")
room['eastCell'].restricted.append("Skeleton Key")
room['northCell'].restricted.append("Skeleton Key")


# Riddles

riddles = [Riddle("What can travel around the world while staying in a corner?", "stamp"), Riddle("What has a bottom at the top?", "legs"), Riddle(
    "I am an odd number. Take away a letter and I become even. What number am I?", "seven"), Riddle("I'm tall when I'm young and I'm short when I'm old. What am I?", "candle"), Riddle("What has hands but can not clap?", "clock")]
