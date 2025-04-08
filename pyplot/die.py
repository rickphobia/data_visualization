from random import randint

class Dies:
    def __init__(self, sides = 6):
        self.sides = int(sides)

    def roll(self):
        return randint(1,self.sides)        