from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

name = input("Name your character: ")

player = Player(name, room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

options = ["n", "e", "s", "w", "q", "h"]

directions = ["n", "e", "s", "w"]

divider = "\n-----------------------------------------------------\n\n"


print(divider, player, divider)

input("Press Enter to continue...")

active = True

while active == True:
    print(divider,
          f"You are located at the {player.curr_room.name}. \n{player.curr_room.att}")
    cmd = input("Which way shall we venture? ")
    location = getattr(player.curr_room, str(f"{cmd}_to"))
    if cmd not in options:
        print("That isn't a valid command. Enter a command to continue. \nCommands: \nn => Go North \ne => Go East \ns => Go South \nw => Go West \nh => Help \nq => Quit\n\n", divider)
    elif cmd == "h":
        print("HELP \nCommands: \nn => Go North \ne => Go East \ns => Go South\n w => Go West \nh => Help \nq => Quit\n\n", divider)
    elif cmd == "q":
        active = False
    else:
        if location == None:
            print("You cannot turn that way. Please try again.")
    player.curr_room = location

if active == False:
    print("Thanks for playing!\n\n", divider, divider, divider)
