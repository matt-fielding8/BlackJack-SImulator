import funlib as lib
import random as rd

deck = {'A': [1, 11], '2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7': [7], '8': [8], \
                 '9': [9], '10': [10], 'J': [10], 'Q': [10], 'K': [10]}

print(lib.player_info())
print(rd.choice(list(deck.keys())))



