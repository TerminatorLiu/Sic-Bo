import random

Odds = {
    'BigSmall':1
}

class Sic_Bo():
    def __init__(self):
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.dice3 = Dice()

    def open(self):
        self.dice1.roll()
        self.dice2.roll()
        self.dice3.roll()

    def income(self,bet,game_type,*args):
        if game_type == 'BigSmall':
            return Odds[game_type]*bet if self.BigSmall(args[0]) else -bet
        else:
            return 0
    def BigSmall(self,val):
        '''
        0:small
        1:big
        '''
        if self.dice1.points == self.dice2.points and self.dice2.points == self.dice3.points:
            return 0
        elif self.dice1.points + self.dice2.points + self.dice3.points < 11:
            return val == 0
        else:
            return val == 1

class Dice():
    def roll(self):
        self.points = random.randint(1,6)
