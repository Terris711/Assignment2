from random import randint

class Items():
   
    WIDTH = 100
    HEIGHT = 100

    def __init__(self, itemTypes):
        self.itemTypes = itemTypes
        x = randint(0, self.WIDTH)
        y = randint(0, self.HEIGHT)
        self.location = (x, y)
        

