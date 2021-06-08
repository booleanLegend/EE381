import random

p = 0.5 # A fair coin.

game = [] # Record of game.

Coin = 0 # Initial value.

win = 0 # Accumulator variable for the number of games won

N = 10000 # Number of times to repeat experiment.

for i in range(N):
    Coin = 0 # Reset
    while Coin != 1:
        r = random.uniform(0,1)
        if r < p:
            Coin = 0 # Tails.
        else:
            Coin = 1 # Heads.
        game.append(Coin) # Record of flips for a single game.

    L = len(game) # The length of a run for an individual game.

    if L % 2 == 1: # Was the head on an odd flip?
        win = win + 1 # If heads on an odd flip increment accumulator.

    game = [] # Reset

print('The probability of the first head on an odd flip is',win / N,'.')