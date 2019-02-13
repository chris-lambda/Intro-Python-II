# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room, pack, limit):
        self.room = room
        # TODO player can carry items
        self.inv = []
        self.pack = pack
        self.limit = limit
    
    #TODO player can pickup items
    def get(self, item):
        self.inv.append(item)
        self.pack = self.pack + item.weight


    #TODO player can frop items
    def drop(self, index):
        self.pack = self.pack - self.inv[index].weight
        del self.inv[index]
