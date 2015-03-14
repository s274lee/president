'''
Created on Mar 13, 2015

@author: sharon
'''
import random    # used to randomly shuffle the deck


# Shuffles an array of 54 ints which represent the cards
# Input: None
# Returns a list of int
def shuffledeck():
    
    # Build the deck
    deck = range(1,53)
    deck.append(53)
    deck.append(53)
    
    # Shuffle the deck
    random.shuffle(deck)
    
    return deck

# Figures out whether player's suggested play is valid
# Input: list of int, list of int
# Returns a boolean
def caniplay(mycards, currentplay):
    
    # Make sure all cards have the same number (3, 4, ... 2, Joker)
    cardnumber = max(mycards) // 4
    for each in mycards:
        if each // 4 != cardnumber:
            return False
    
    # Handle Joker case
    if mycards[0] == 53:
        if (len(mycards)*2 >= len(currentplay)):
            return True
    else:
        
        # Handle regular case
        if ((len(mycards) == len(currentplay))
            and max(mycards) >= max(currentplay)):
            return True
        else:
            return False


