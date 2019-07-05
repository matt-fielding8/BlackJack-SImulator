import numpy as np
import pandas as pd
import random as rd

# def card_decks(n):
#     '''' (int) -> list of lists
#
#     Creates n number of card decks arrays consisting of 4 suited sets, with card id at index 0 and card value at index [1:].
#
#     >>> card_decks(1):
#     [[[['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]],
#     [['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]],
#     [['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]],
#     [['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7], [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]]]
#     '''
#
#     playing_deck = []
#     card_array = [['A', 1, 11], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7],
#                    [8, 8], [9, 9], [10, 10], ['J', 10], ['Q', 10], ['K', 10]]
#
#     if n != 0:
#         for i in range(n*4):
#             playing_deck.append(card_array)
#     else:
#         return "Zero is not a valid number of card decks"
#
#
#     return playing_deck

def playing_deck(n):
    ''' (int) -> list of dicts

    Creates a list of n*4 dicts with car_id's as keys and values as list a list of corresponding card values.

    >>> card_decks():
    [{'A': [1, 11], '2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7': [7], '8': [8],\
        '9': [9], '10': [10], 'J': [10], 'Q': [10], 'K': [10]}
    {'A': [1, 11], '2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7': [7], '8': [8],\
        '9': [9], '10': [10], 'J': [10], 'Q': [10], 'K': [10]}
    {'A': [1, 11], '2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7': [7], '8': [8],\
        '9': [9], '10': [10], 'J': [10], 'Q': [10], 'K': [10]}
    {'A': [1, 11], '2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7': [7], '8': [8],\
        '9': [9], '10': [10], 'J': [10], 'Q': [10], 'K': [10]}]
    '''

    playing_deck = []
    card_dict = {'A': [1, 11], '2': [2], '3': [3], '4': [4], '5': [5], '6': [6], '7': [7], '8': [8], \
                 '9': [9], '10': [10], 'J': [10], 'Q': [10], 'K': [10]}

    if n !=0:
        for _ in range(n*4):
            playing_deck.append(card_dict)
        return playing_deck
        # return [playing_deck.append([12]) for i in range(n*4)]
    else:
        return "ERROR: Zero is not a valid number of card decks"


def player_info():
    ''' () -> dict {player: score}

    Prompt the user to enter payer names, return a dict of player names and card hand total.
    '''

    player_dct = {}
    player = input('Enter player name: ')


    while player != 'p':
        if player in player_dct:
            print('Player {player} is already playing.'.format(player = player))

        if player not in player_dct:
            player_dct[player] = ''

        player = input("Enter player name (or 'p' to play): ")

    player_dct['Dealer'] = ''

    return player_dct

def select_card(card_deck):
    ''' (list of lists) -> list [str, int]

    Selects one random card from the list cards and returns its corresponding id and value.
    '''

    card = []
    #Generate random numbers for indexing

    rand1 = rd.randint(0, len(card_deck)-1)
    rand2 = rd.randint(0, len(card_deck[rand1])-1)

    #Retrieve random card information from card_deck array
    card.extend(card_deck[rand1][rand2])


    return card

def select_card_value(card):
    ''' (list [str, int]) -> int

    Returns the value of card.

    >>> select_card_value(['J', 10])
    10
    >>> select_card_value(['6', 6])
    6
    '''

    card_value = card[-1]

    return card_value

def select_card_id(card):
    ''' (list [str, int]) -> str

    Returns the id of card.

    >>> select_card_id(['J', 10])
    'J'
    >>> select_card_id(['6', 6])
    '6'
    '''

    card_id = card[0]

    return card_id

def deal_cards(players, deck):
    ''' (dict, list of list) -> list of list [str, str, int]

    Deals 2 random cards from deck for each player in players. Returns each player hand as a string,
    dealer hand showing 1 card only.

    >>> deal_cards(players, deck):
    [['ding:', 'A J', 20], ['dong:', '2 3', 5], ['Dealer:', 'K', 10]]
    '''







