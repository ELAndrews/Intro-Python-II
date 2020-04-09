from room import Room
from game_manager import room
from player import Player
from item import Tool, Weapon, Coins

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

options = ["n", "e", "s", "w", "q", "h", "l"]

directions = ["n", "e", "s", "w"]

divider = "\n-----------------------------------------------------\n\n"


print(divider, player, divider)

input("Press Enter to continue...")

active = True

while active == True:
    print(divider,
          f"   You are located at the {player.curr_room.name}. \n{player.curr_room.att}")
    cmd = input("What shall we do? ")
    if cmd in options:
        if cmd == "h":
            print("\n\nHELP \nCommands: \nn => Go North \ne => Go East \ns => Go South\nw => Go West \nh => Help \nl => Look around \nq => Quit\n\n", divider)
            input("Press Enter to continue...")
        elif cmd == "q":
            active = False
        elif cmd == "l":
            items = getattr(player.curr_room, "items")
            if len(items) == 0:
                print(
                    "You scan the area... You find nothing you can useful for your quest")
                input("Press Enter to continue...")
            else:
                print(f"You scan the area... You find: {items}")
                input("Press Enter to continue...")
        else:
            location = getattr(player.curr_room, str(f"{cmd}_to"))
            if location == None:
                print("You cannot turn that way. Please try again.")
                input("Press Enter to continue...")
            else:
                player.curr_room = location
    else:
        print("\n\nThat isn't a valid command. Enter a command to continue. \nCommands: \nn => Go North \ne => Go East \ns => Go South \nw => Go West \nh => Help \nq => Quit\n\n", divider)
        input("Press Enter to continue...")

if active == False:
    print(divider, "Thanks for playing!\n\n", divider)
