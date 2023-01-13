import random

def shuffle(deck):
    
    # separate cards randomly into 4 sets
    shuffle1 = []
    shuffle2 = []
    shuffle3 = []
    shuffle4 = []
    
    # copy deck to be shuffled
    to_shuffle = deck.copy()
    
    # select a set of indec numbers to pick from deck
    random_select1 = list(random.sample(range(14), 13))
    random_select2 = list(random.sample(range(14), 13))
    random_select3 = list(random.sample(range(14), 13))
    random_select4 = list(random.sample(range(6), 6))
   
    
    for i in random_select1:
        
        shuffle1.append(to_shuffle[i]) # append randomly selected card to 1st deck
        del to_shuffle[i] # remove the selected card from main deck
    
    for j in random_select2:
        
        shuffle2.append(to_shuffle[j])
        del to_shuffle[j]
       
    for k in random_select3:
        
        shuffle3.append(to_shuffle[k])
        del to_shuffle[k]
        
    for l in random_select4: # Cant figure out but it index gets out of range after few iterations. 
        #I think it is related to after popping, list len() decreases but iteration range stays the same.
        shuffle4.append(to_shuffle[l])
        del to_shuffle[l]
  
        
      #Here comes more eyesore. Distribute remainders between other decks
   
    shuffle1.insert(5, to_shuffle[0])
    del to_shuffle[0]
    shuffle2.insert(3, to_shuffle[0])
    del to_shuffle[0]
    shuffle3.insert(7, to_shuffle[0])
    del to_shuffle[0]
    shuffle4.insert(3, to_shuffle[0])
    del to_shuffle[0]
    shuffle1.append(to_shuffle[0])
    del to_shuffle[0]
    shuffle2.insert(9, to_shuffle[0])
    del to_shuffle[0]    
    shuffle3.insert(10, to_shuffle[0])
    del to_shuffle[0]
        
      
    shuffled = shuffle1 + shuffle2 + shuffle3 + shuffle4
    
    #print(len(shuffle1), shuffle1) #Can check each shuffled deck before joining
    #print(len(shuffle2), shuffle2)
    #print(len(shuffle3), shuffle3)
    #print(len(remainder_added ), remainder_added )
    
    print(*shuffled, sep='\n')
    print("There are,", len(shuffled), "cards in the deck.", "If 'False', there are no duplicates: ", len(shuffled) != len(set(shuffled))) # checking if there are duplicates

