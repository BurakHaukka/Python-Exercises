from shuffler import shuffle

suit = ("Clubs", "Diamonds", "Hearts", "Spades")
value = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
deck = []

for i in range(0, len(value)):
    for j in range(0, len(suit)):
        card = suit[j] + "-" + value[i]
        deck.append(card)


#print(*deck, sep='\n') # This prints list like "for loop"
#print(len(deck))
    


shuffle(deck)