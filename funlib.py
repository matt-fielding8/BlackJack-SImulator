import numpy as np
import pandas as pd

def card_decks(n):
    '''' (int) -> list of lists

    Creates n number of card decks arrays consisting of 4 suited sets, with card id at index 0 and card value at index [1:].

    >>> card_decks(2):
    [[[['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]],
    [['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]],
    [['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]],
    [['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]]]
    '''

    playing_deck = []
    card_array = [['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7],
                   [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]]

    if n != 0:
        for i in range(n*4):
            playing_deck.append(card_array)
    else:
        return "Zero is not a valid number of card decks"


    return playing_deck

print(card_decks(1))