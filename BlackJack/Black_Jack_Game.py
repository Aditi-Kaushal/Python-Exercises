import random

# Function to Calculate Total of Card in Hand
def calculateTotal( cards ):
    total = 0
    ace_found = False
    for card in cards:
        if card[0] >= 1 and card[0] <= 10:
            total += card[0]
        elif card[0] == 11 or card[0] == 12 or card [0] == 13:
            total += 10
        if card[0] == 1:
            ace_found = True
    if ace_found and total < 16 and ( total + 10 ) <= 21:
        total += 10
    return total

# Function to Calculate Total of Dealer Card in Hand
def calculateDealerCardTotal( cards ):
    total = 0
    ace_found = False
    first_card = True
    for card in cards:
        if first_card:
            first_card = False
        else:
            if card[0] >= 1 and card[0] <= 10:
                total += card[0]
            elif card[0] == 11 or card[0] == 12 or card [0] == 13:
                total += 10
            if card[0] == 1:
                ace_found = True
    if ace_found and total < 16 and ( total + 10 ) <= 21:
        total += 10
    return total


# Function to prepare a String according to Card given
def prepareCardString( card ):
    output = " { "
    if card[0] == 1:
        output += "Ace"
    elif card[0] == 11:
        output += "Jack"
    elif card[0] == 12:
        output += "Queen"
    elif card[0] == 13:
        output += "King"
    else:
        output += str(card[0])
    output += " of " + card[1] +" }"
    return output

def displayDealerCard( cards ):
    output = " Dealer Cards: "
    first_card = True
    for card in cards:
        if first_card:
            output += " { Folded }"
            first_card = False
        else:
            output += prepareCardString(card)
    output += " Total Rank: " + str(calculateDealerCardTotal(cards))
    print(output)

def displayCards(cards,playername):
    output = " " + str(playername) + " Cards: "
    for card in cards:
        output += prepareCardString(card)
    output += " Total Rank: " + str(calculateTotal(cards))
    print(output)

def displayLine():
    output = ""
    count = 1
    while count <= 120:
        output += "-"
        count += 1
    print(output)


# We know Suit are of Four Type
suits = ("Heart","Diamond","Spade","Club")
# I need to construct a Deck which have 52 Cards
# Every Card have two value one is its Face Value and Suit
deck = []
# Generate 13 Card of Every Suit and save them inside deck list in form of tuple
# List of Tuples concept
for suit in suits:
    face = 1
    while face <= 13:
        deck.append( (face,suit) )
        face += 1

# Shuffle the Deck
count = 1
while count <= 1000:
    # Generate a random index between 1 and 51
    index = random.randint(1,51)
    # Interchange the First Card present in Deck with index number Card
    temp = deck[0]
    deck[0] = deck[index]
    deck[index] = temp
    count += 1

# List for Player Card in Hand
player_cards = []
# List for Dealer Card in Hand
dealer_cards = []

amount = int(input(" Enter Bet Amount: "))

# Remove Two Top Card and Add in to Player Cards
player_cards.append( deck.pop() )
player_cards.append( deck.pop() )
# Remove Two Top Card and Add in to Dealer Cards
dealer_cards.append( deck.pop() )
dealer_cards.append( deck.pop() )

displayLine()
displayCards(player_cards,"Player")
displayDealerCard(dealer_cards)

if calculateTotal(player_cards) == 21:
    print(" BLACK JACK ")
    print(" Player Wins!!! Amount Rs.", amount)
else:
    while True:
        displayLine()
        print(" Press 1 For Hit a Card ")
        print(" Press 2 For Stand ")
        displayLine()
        choice = int(input(" Enter Your Choice: "))
        displayLine()
        if choice == 1:
            # Remove Top Card and Add in to Player Cards
            player_cards.append(deck.pop())
            displayCards(player_cards,"Player")
            if calculateTotal(player_cards) > 21:
                displayLine()
                print(" PLAYER IS BUSTED SO LOSE AMOUNT Rs.",amount)
                break
        elif choice == 2:
            displayCards(player_cards,"Player")
            displayCards(dealer_cards,"Dealer")
            displayLine()
            player_total = calculateTotal(player_cards)
            dealer_total = calculateTotal(dealer_cards)
            while dealer_total < 16 and dealer_total < player_total:
                dealer_cards.append(deck.pop())
                displayCards(player_cards, "Player")
                displayCards(dealer_cards, "Dealer")
                displayLine()
                dealer_total = calculateTotal(dealer_cards)
            if dealer_total > 21:
                print(" DEALER LOSE PLAYER WON AMOUNT Rs.",amount)
            elif dealer_total == player_total:
                print(" NO WIN NO LOSE MEANS TIE ")
            elif dealer_total > player_total:
                print(" DEALER WINS PLAYER LOSE AMOUNT Rs.",amount)
            else:
                print(" PLAYER WON AMOUNT Rs.",amount)
            break
        else:
            print(" Invalid Choice Try Again ")

displayLine()

