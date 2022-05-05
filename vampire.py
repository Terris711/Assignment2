from vampiHuman import VampiHuman


class Vampire(VampiHuman):

    def __init__(self, *arrs):
        super().__init__(arrs)

    def moving(self):
        # Vampire can move 8 steps
        for i in range(8):
            super().moving()
