from const import NEEDLE, ETHER, TUBE, FLOOR


class Object():
    def __init__(self, ITEM):
        self.item = ITEM
        self.ispicked = False
    def str_repr(self, item):
        if self.ispicked is True :
            return FLOOR
        else :
            return item
    def status(self, status):
        print("PICKED")
        self.ispicked = status
    