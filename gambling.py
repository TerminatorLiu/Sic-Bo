from sic_bo import Sic_Bo

class Gambling():
    def __init__(self,initial_funding):
        self.initial_funding = initial_funding
        self.sic_bo = Sic_Bo()
        self.final_funding = self.initial_funding

    def reset(self,initial_funding):
        self.initial_funding = initial_funding
        self.final_funding = self.initial_funding

    def simulate(self):
        iter = 0
        while(iter<100 and self.final_funding>10):
            self.sic_bo.open()
            self.final_funding += self.sic_bo.income(10,'BigSmall',0)
            iter += 1
        return 0

    def income(self):
        return self.final_funding - self.initial_funding
