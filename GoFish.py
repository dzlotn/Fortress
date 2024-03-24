
import random
#prints the game rules
def goFish():
    print("Welcome to Go fish! Here are the rules: if you are dealt a four of a kind, or get a four of a kind during game play, that is called a book, and those cards are removed from your hand and you get a point. Moving clockwise, players take turns asking a specific player for a specific card.")
    print("For example, Player One may ask Player Two for an Ace, or someone asks you for a card that you have.")
    print("all cards that match that value are taken from your hand. if you do not have any cards of that rank, your opponent must go fish, taking one new card from the pile of cards.")
    print("if you run out of cards and there are stil cards left, you get five free cards, and play continues until all hands are empty and there are no more cards to draw from. The winner is the player with the most points at the end.")

#creates the deck of cards and shuffles it.
def createDeck():  
    deck=['A','A','A','A','2','2','2','2', '3','3','3','3','4','4','4','4','5','5','5','5','6','6','6','6', '7','7','7','7'  ,'8','8','8','8','9','9','9','9','10','10','10','10','J','J','J','J','Q','Q','Q','Q','K','K','K','K']
    random.shuffle(deck)
    return deck

#Deals 5 cards to each player, removing those dealt cards from the deck. Prints each player’s deck and returns the number of cards in the deck.
def dealCards(deck):
    p1=[]
    card=0
    while card<5:
        p1.append(deck[0])
        deck.pop(0)
        card=card+1
    p2=[]
    card2=0
    while card2<5:
        p2.append(deck[0])
        deck.pop(0)
        card2=card2+1
    print("Player 1: your hand is:")
    print(p1)
    print("Player 2: your hand is")
    print(p2)
    print("There are {} cards in the deck".format(len(deck)))
    hands = (p1,p2) 
    return hands
 
# Verifies that a player has four of the specified card from their deck.
def checkdeck(asked,playerdeck):
    samecards=0
    for card in playerdeck:
        if card==asked:
            samecards+=1
    if samecards==4:
	    return True
    else:
        return False

 #Runs the game. Creates score variables, deals with the cards (adding, transferring, and removing), and ends the game.
def playGame(deck, hands):
    p1 = hands[0]
    p2 = hands[1]
    #create score variables
    p1Score=0
    p2Score=0
    run = True
    while (run):
        if len(p1) ==0:
            card=0
            while card<5:
                p1.append(deck[0])
                deck.pop(0)
                card=card+1
            print(" Player 1: you just received 5 new cards. Your new hand is: " + p1)
        if len(p2) ==0:
            card=0
            while card<5:
                p2.append(deck[0])
                deck.pop(0)
                card=card+1
            print(" Player 2: you just received 5 new cards. Your new hand is: " + p2)
    

        askedcard = input("Player 1: what card do you want to ask player 2? ").upper()
        if askedcard in p2:
            tempP2=[]
            for card in p2:
                if askedcard == card:
                    p1.append(askedcard)
                else:
                    tempP2.append(card)
            p2=[] 
            p2 = list(tempP2)  
            print("Player 2 has the card")
            print("Player 1: your hand is:")
            print(p1)
            print("Player 2: your hand is")
            print(p2)

        else:
            print("Player 2 does not have that card. GO FISH!!")
            p1.append(deck[0])
            deck.pop(0)
            print("Player 1: your hand is:")
            print(p1)
            print("Player 2: your hand is:")
            print(p2)
       
 #PLAYER TWO'S TURN
        askedcard = input("Player 2: what card do you want to ask player 1? ").upper()
        if askedcard in p1:
            tempP1=[]
            for card in p1:
                if askedcard == card:
                    p2.append(askedcard)
                else:
                    tempP1.append(card)
                 
            p1= []  
            p1= list(tempP1) 
            print("Player 1: your hand is:")
            print(p1)
            print("Player 2: your hand is")
            print(p2)
        else:
            print("player 1 does not have that card. GO FISH!!")
            p2.append(deck[0])
            deck.pop(0)
            print("Player 1: your hand is: ")
            print(p1)
            print("Player 2: your hand is: ")
            print(p2)
	      
        newPlayerOne =[]
        x =0
        book=input("Player 1: What cards do you want to discard? If you don't think you have four of a pair, type in a random card" ).upper()
        if(checkdeck(book, p1)):
            p1Score+=1
            print("You have four of that card")
            print("Player 1: Your score is now {}".format(p1Score))
            while x<len(p1):
                bk=p1[x]
                if bk != book:
                    newPlayerOne.append(bk)
                x=x+1
            p1= list(newPlayerOne)
        else:
            print("You don't have four of that card")   
        newPlayerTwo =[]
        x =0
        book=input("Player 2: What cards do you want to discard? If you don't think you have four of a pair, type in a random card" ).upper()
        if(checkdeck(book, p2)):
            p2Score+=1
            print("You have four of that card")
            print("Player 2: Your score is now {}".format(p2Score))
            while x<len(p2):
                bk=p2[x]
                if bk != book:
                    newPlayerTwo.append(bk)
                x=x+1
            p2= list(newPlayerTwo)
        else:
	        print("You don't have four of that card")
        
        if len(deck)<=5:
            print("There are now less than 5 cards. Calculating Scores.... ")
            run = False
            if p1Score==p2Score:
	            print("Both players tied")
            elif p1Score>p2Score:
	            print("Player 1 wins!")
            else: 
	            print("Player 2 wins!")
  
        if len(p1) ==0:
            card=0
            while card<5:
                p1.append(deck[0])
                deck.pop(0)
                card=card+1
            print(" Player 1: you just received 5 new cards. Your new hand is: " + p1)
        if len(p2) ==0:
            card=0
            while card<5:
                p2.append(deck[0])
                deck.pop(0)
                card=card+1
            print(" Player 2: you just received 5 new cards. Your new hand is: " + p2)
    
	
goFish()
deck=createDeck()
hands=dealCards(deck)
playGame(deck,hands)

