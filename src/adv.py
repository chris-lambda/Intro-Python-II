from room import Room
from player import Player
from item import Item
import random
# Declare all the rooms

items = [
    Item("Grass" , 1),
    Item("Dirt" , 2),
    Item("Pearl" , 5),
    Item("Diamond" , 7),
    Item("Wood" , 3),
    Item("Rock" , 4),
]

def getRandomItems(itms):
    def rIndex():
        return random.randint(0, len(itms) - 1)
    rItems = [
        itms[rIndex()],
        itms[rIndex()],
        itms[rIndex()],
        itms[rIndex()],
        itms[rIndex()],
    ]

    return rItems

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                        getRandomItems(items)
                    ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                        getRandomItems(items)
                        ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                        getRandomItems(items)
                        ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                        getRandomItems(items)
                        ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                        getRandomItems(items)
                        ),
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
p = Player(room['outside'], 0, 15)

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

dir = ["w", "a", "s", "d"]
error = ""

while True:
    roomItems = ', '.join([x.name for x in p.room.inv])
    playerInv = [x.name for x in p.inv] if len(p.inv) else "Empty"

    print("""
Controls 
    get <item name>
    drop <item name>
    w: go north
    a: go west
    s: go south
    d: go east
""")

    print(f"Location: {p.room.name}")
    print(f"Hint: {p.room.description}")
    print(f"Bag: {p.pack}/{p.limit}")
    print(f"Inventory: {playerInv}")
    print(f"Surroundings: {roomItems}")
    print(error)
    error = ""

    action = input(">> ")
    items = action.split()[1:]
    if action.startswith("get "):
        if len(items) > 1:
            error = "Only one item at a time"
        else:
            iNames = [x.name for x in p.room.inv]
            itemIndex = iNames.index(items[0])
            p.get(p.room.inv[itemIndex])
            p.room.drop(itemIndex)


    elif action.startswith("drop "):
        if len(items) > 1:
            error = "Only one item at a time"
        else:
            iNames = [x.name for x in p.inv]
            itemIndex = iNames.index(items[0])
            p.room.get(p.inv[itemIndex])
            p.drop(itemIndex)


    elif action in dir:
        if action == 'w':
            if hasattr(p.room, 'n_to'):
                p.room = p.room.n_to
            else:
                error = f"Oops nothing there still at {p.room.name}"
                
        elif action == 's':
            if hasattr(p.room, 's_to'):
                p.room = p.room.s_to
            else:
                error = f"Oops nothing there still at {p.room.name}"
        elif action == 'a':
            if hasattr(p.room, 'e_to'):
                p.room = p.room.e_to
            else:
                error = f"Oops nothing there still at {p.room.name}"
        elif action == 'd':
            if hasattr(p.room, 'w_to'):
                p.room = p.room.w_to
            else:
                error = f"Oops nothing there still at {p.room.name}"
    # elif action == "i":    
    else: 
        print("Please enter proper command look at controls")