#import matplotlib.pyplot as plt
from gambling import Gambling
game = Gambling(initial_funding = 1000)
result = []
for i in range(0,10):
    game.simulate()
    result.append(game.income())
    game.reset(initial_funding = 1000)

print(result)
print(sum(result))



