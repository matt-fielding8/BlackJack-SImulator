# BlackJack_Game
BlackJack is a card game commonly played in Casinos where a players aim is to
achieve a score of 21 or fewer whilst accumulating a total which is greater than
the dealer total. This repositiory holds that starter code for the game, which
_does not_ yet have all the functions necessary to drive the game.

The first goal is to code the game, complete with all traditional rules, which
enables multiple players to play the game, and make some customisations such as
choosing the number of standrd 52 card decks form the main playing deck.

Once this is achieved, the aim is to simulate many thousands of games to collect
playing data from each hand. Supervised machine learning algorithms can then be
applied to identify the most effective strategies.

## Usage
Currently not all of the necessary functions have been written to establish
game play. When they have it will be necessary to download the `funlib.py` and
`game.py` libraries. `game.py` will be the main driver for gameplay.

## Libraries
The main libraries that have been set up so far:
* `funlib.py` - This library holds all of the functions needed
* `funtest.py` - This library is used as a testing environment for the functions
in `funlib.py`
* `game.py` - This library is used as the driver for the game.
