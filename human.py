from random import randint

from vampiHuman import VampiHuman


class Human(VampiHuman):
    myClass = "Human"
    age = 0
    step = 0
    health = 100

    def __init__(self, *arrs):
        super().__init__(arrs)
        self.age = randint(10, 50)

    # if the function returns True, human can move
    # if the function returns False, human is dead

    def moving(self):
        # Human can only move 4 steps
        for i in range(4):
            super().moving()
            self.health -= 1
            self.age += 1
            self.step += 1

        if self.step > 70:
            return False
        else:
            return True

    # Attacking
    def human_attack(self):
        self.health += 20

    # Being attacked

    def human_attacked(self):
        self.health -= 20

    def human_help(self):
        self.health += 10
