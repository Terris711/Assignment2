from random import randint


class VampiHuman:
    myClass = "VampiHuman"
    location = (0, 0)
    # if both human and vampire do not interact, they continue moving
    interact = False

    WIDTH = 100
    HEIGHT = 100

    def __init__(self, *arrs):
        check = True
        while check:
            x = randint(0, self.WIDTH)
            y = randint(0, self.HEIGHT)
            self.location = (x, y)
            for arr in arrs:
                if self.location in arr:
                    check = True
                else:
                    check = False

    def moving(self):

        # move to random location
        moveIndex = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        check = True
        while (check):
            index = randint(0, 3)
            x1 = self.location[0] + moveIndex[index][0]
            y1 = self.location[1] + moveIndex[index][1]
            if x1 > self.WIDTH or x1 < 0 or y1 > self.HEIGHT or y1 < 0:
                check = True
            else:
                check = False
                self.location = (x1, y1)
