from item import Item
# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.inv = items
        # TODO have room hold items
    
    # TODO room can get items
    def get(self, item):
        self.inv.append(item)

    # TODO room can drop items
    def drop(self, index):
        del self.inv[index]

    
