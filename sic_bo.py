
class Sic_Bo():
    def __init__(self):
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.dice3 = Dice()

    def open(self):
        self.dice1.roll()
        self.dice2.roll()
        self.dice3.roll()

    def income(self,bet,type,*args):
        return 0

class Dice():
    def roll(self):
        return 0
