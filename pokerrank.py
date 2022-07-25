import random

#create deck of cards
names = ['1','2','3','4','5','6','7','8','9','10', 'Jack', 'Queen', 'King']
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

def createADeck():
    deck = []
    for s in suits:
        for v in names:
            deck.append((v,s))
    return deck

deck = createADeck()

#card combinations, now you must figure out how to get the computer to differentiate b/t the different card levels
for i in range(0,5):    
    print(random.choice(deck))

#if all values above 10 are in order it's a royal flush 10pts
#if all values below 10 are in order it is a straight flush 9pts
#if 3 names are the same and 2 others are also the same it is 4 of a kind 8pts

#create card combinations list 5 values from the deck list in function createaDeck
#list the values of the card combinations by score 
#run program to display 5 random hands and have user input what is the highest value 