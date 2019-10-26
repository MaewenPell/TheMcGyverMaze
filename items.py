from const import NEEDLE, ETHER, TUBE

class Object():
    def __init__(self, ITEM):
        self.item = ITEM
    def repr(self, item):
        return item
    def status(self, status):
        self.ispicked = status
    