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

#create card combinations 