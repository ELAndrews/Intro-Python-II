from room import Room
from game_manager import room, riddles
from player import Player
from item import Tool, Weapon, Coins
import random

#
# Main
#

# Make a new player object that is currently in the 'outside' room.


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

#  ---------------------------- Initial Variables ---------------------------- #

options = ["n", "e", "s", "w", "q", "h", "l"]
directions = ["n", "e", "s", "w"]
divider = "\n-----------------------------------------------------\n\n"
active = True


#  ---------------------------- Game Start ---------------------------- #

name = input("Name your character: ")
player = Player(name, room['outside'])

print(divider, player, divider)
input("Press Enter to continue...")


#  ---------------------------- Game Functions ---------------------------- #

def my_inventory():
    my_items = getattr(player, "inventory")
    if len(my_items) == 0:
        print("You have nothing in your inventory.")
        return False
    elif len(my_items) == 3:
        print("Your inventory is full.")
        print("You currently have:  ")
        for item in my_items:
            print(f"{item.name}")
        return True
    else:
        print("You currently have:  ")
        for item in my_items:
            print(f"{item.name}")
        return False


def riddle():
    print("Answer my riddle correctly and proceed. Answer it wrong and you must turn back")
    riddle = random.choice(riddles)
    answer = input(f"{riddle.question}  ")
    if answer == riddle.answer:
        print("hmm... you are wiser than I thought. You may enter.")
        input("Press enter to move on")
        return True
    else:
        print("Mwhahaha ... you are wrong little one. Return from whence you came")
        input("Press enter to move on")
        return False


def pick_up_action():
    items = getattr(player.curr_room, "items")
    bag = my_inventory()
    if bag == True:
        print("\nTo pick up an item, you need to drop something first.")
    else:
        space = 3 - len(player.inventory)
        print(f"You have space for {space} item(s)")
        print(f"Select an item to pick up: ")
        i = 1
        for item in items:
            print(f"{i} => {item.name}: {item.description}")
            i += 1
        selection_valid = False
        while selection_valid == False:
            selection = input("Enter the items: ").lower()
            item = [item for item in items if item.name.lower() == selection]
            if len(item) == 0:
                print("Sorry, that was a valid selection. Try again")
                pass
            else:
                if item[0].name == "Gold Coins":
                    player.gold += item[0].amount
                    print(f"You now have {player.gold} Gold Coins")
                else:
                    player.inventory.append(item[0])
                    print(f"You are now carrying the {item[0].name}")
                item_i = player.curr_room.items.index(item[0])
                player.curr_room.items.pop(item_i)
                selection_valid = True


def pick_up():
    valid = True
    while valid == True:
        action = input("\nDo you want collect an item? y/n  ")
        if action == "n":
            valid = False
            pass
        elif action == "y":
            valid = False
            pick_up_action()
        else:
            print("Sorry, I don't understand.")


def drop():
    selection_valid = False
    bag = my_inventory()
    while selection_valid == False:
        selection = input("Which item do you want to drop? ").lower()
        item = [item for item in player.inventory if item.name.lower()
                == selection]
        item_i = player.curr_room.items.index(item[0])
        player.inventory.pop(item_i)
        player.curr_room.items.append(item)
        print(f"You have just dropped your {item[0].name}")

# def use


def look():
    items = getattr(player.curr_room, "items")
    if len(items) == 0:
        print("\nYou scan the area... \nYou find nothing you can useful for your quest")
        input("\n\nPress Enter to continue...")
    else:
        print(f"\nYou scan the area... \nYou find:")
        for item in items:
            print(f"{item.name}")
        pick_up()

        input("\n\nPress Enter to continue...")


def move():
    location = getattr(player.curr_room, str(f"{cmd}_to"))
    if location == None:
        print("\nYou cannot turn that way. Please try again.")
        input("\nPress Enter to continue...")
    elif location.locked == True:
        if location.name == "The Gate Keep":
            player.curr_room = location
            access = riddle()
            if access == True:
                player.curr_room = room['hall']
            else:
                pass
        else:
            print(
                f"To pass this way you need the {location.restricted}, to access {location.name}")
            if location.restricted in player.inventory:
                x = input(f"should we try your {location.restricted}? y/n ")
                if x == "y":
                    pass
                else:
                    pass
    else:
        player.curr_room = location


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
            look()
        else:
            move()
    else:
        print("\n\nThat isn't a valid command. Enter a command to continue. \nCommands: \nn => Go North \ne => Go East \ns => Go South \nw => Go West \nh => Help \nq => Quit\n\n", divider)
        input("Press Enter to continue...")

if active == False:
    print(divider, "Thanks for playing!\n\n", divider)
