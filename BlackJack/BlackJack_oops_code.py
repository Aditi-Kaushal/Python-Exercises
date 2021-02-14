import random

# Card class is used to represent a Card which have two data member
# One is face value of Card and Another is Suit Value
class Card:
    def __init__(self,face,suit):
        self.face =  face
        self.suit = suit
        self.foldStatus = False

    def setFolded(self,status):
        self.foldStatus = status

    def getStringForm(self):
        output = " { "
        if self.foldStatus:
            output += "Folded"
        else:
            if self.face == 1:
                output += "Ace"
            elif self.face == 11:
                output += "Jack"
            elif self.face == 12:
                output += "Queen"
            elif self.face == 13:
                output += "King"
            else:
                output += str(self.face)
            output += " of " + self.suit
        output  += " }"
        return output

# Deck Class is used to represent Deck of Cards i.e. 52 Cards
# This class also provide Function to shuffle it.
class Deck:
    def __init__(self):
        self.suits = ("Heart","Club","Diamond","Spade")
        self.cards = [] # List of Cards
        self.generateCardList()
        self.shuffleDeck()

    def generateCardList(self):
        for suit in self.suits:
            face = 1
            while face <= 13:
                # Add Card class object into list of Cards
                self.cards.append(Card(face, suit))
                face += 1

    def shuffleDeck(self):
        # Shuffle the Deck
        count = 1
        while count <= 1000:
            # Generate a random index between 1 and 51
            index = random.randint(1, 51)
            # Interchange the First Card present in Deck with index number Card
            temp = self.cards[0]
            self.cards[0] = self.cards[index]
            self.cards[index] = temp
            count += 1

    def pickTopCard(self):
        return self.cards.pop()

# Class to Represent a Player
class Player:

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount
        self.cardsInHand = []

    def addCard(self,card):
        self.cardsInHand.append(card)

    def getAmount(self):
        return self.amount

    def updateAmount(self,amount):
        self.amount += amount

    def getName(self):
        return self.name

    def updateCardFoldedStatus(self,status):
        for card in self.cardsInHand:
            card.setFolded(status)

    def clearCardsInHand(self):
        self.cardsInHand.clear()

    def calculateCardTotalRank(self):
        total = 0
        ace_found = False
        for card in self.cardsInHand:
            if not card.foldStatus:
                if card.face >= 1 and card.face <= 10:
                    total += card.face
                elif card.face == 11 or card.face == 12 or card.face == 13:
                    total += 10
                if card.face == 1:
                    ace_found = True
        if ace_found and total < 16 and (total + 10) <= 21:
            total += 10
        return total

    def isBusted(self):
        return self.calculateCardTotalRank() > 21

    def getPlayerDetails(self):
        output = " " + self.name + " Cards: "
        for card in self.cardsInHand:
            output += card.getStringForm()
        output += " Total Rank: " + str(self.calculateCardTotalRank())
        return output

class Game:
    def __init__(self,name,amount):
        self.player = Player(name,amount)
        self.dealer = Player("Dealer",0)

    def displayDetails(self):
        print(self.player.getPlayerDetails())
        print(self.dealer.getPlayerDetails())

    def displayPlayerAmount(self):
        print(" You Have Rs. " + str(self.player.getAmount()) + " in Account")

    def isPlayerBusted(self):
        return self.player.isBusted()

    def isDealerBusted(self):
        return self.dealer.isBusted()

    def getPlayerTotal(self):
        return self.player.calculateCardTotalRank()

    def getPlayerAmount(self):
        return self.player.getAmount()

    def getDealerTotal(self):
        return self.dealer.calculateCardTotalRank()

    def unfoldDealerCards(self):
        self.dealer.updateCardFoldedStatus(False)

    def updatePlayerAmount(self,amount):
        self.player.updateAmount(amount)

    def pickCardForPlayer(self):
        card = self.deck.pickTopCard()
        self.player.addCard(card)

    def pickCardForDealer(self,status):
        card = self.deck.pickTopCard()
        card.setFolded(status)
        self.dealer.addCard(card)

    def startGame(self,bet):
        self.bet = bet
        self.deck = Deck()
        self.player.clearCardsInHand()
        self.dealer.clearCardsInHand()
        # Pick Top Card and Add to Player Card in Hand
        self.pickCardForPlayer()
        # Pick Top Card and Add to Dealer Card in Hand
        self.pickCardForDealer(True)
        # Pick Top Card and Add to Player Card in Hand
        self.pickCardForPlayer()
        # Pick Top Card and Add to Dealer Card in Hand
        self.pickCardForDealer(False)

class Utility:
    def displayLine(self):
        output = ""
        count = 1
        while count <= 120:
            output += "-"
            count += 1
        print(output)

# Main Code Begin
utility = Utility()
utility.displayLine()
name = input(" Enter Player Name: ")
amount = int(input(" Enter Amount: Rs. "))
game = Game(name,amount)
while True:
    utility.displayLine()
    print(" Press 1 For Start a New Game: ")
    print(" Press 2 For Display Account ")
    print(" Press 3 For Exit ")
    utility.displayLine()
    choice = int(input(" Enter Your Choice: "))
    utility.displayLine()
    if choice == 1:
        bet = int(input(" Enter Bet Amount: Rs. "))
        utility.displayLine()
        if bet <= game.getPlayerAmount():
            game.startGame(bet)
            if game.getPlayerTotal() == 21:
                game.unfoldDealerCards()
                game.displayDetails()
                utility.displayLine()
                if game.getPlayerTotal() == game.getDealerTotal():
                    print(" BLACKJACK IN TIE MODE ")
                else:
                    game.updatePlayerAmount(bet * 1.5)
                    print(" BLACKJACK PLAYER WINS ")
            else:
                game.displayDetails()
                while True:
                    utility.displayLine()
                    print(" Game Options ")
                    print(" Press 1 For Hit ")
                    print(" Press 2 For Stand ")
                    utility.displayLine()
                    choice = int(input(" Enter Player Choice: "))
                    if choice == 1:
                        game.pickCardForPlayer()
                        utility.displayLine()
                        game.displayDetails()
                        if game.isPlayerBusted():
                            utility.displayLine()
                            game.unfoldDealerCards()
                            game.displayDetails()
                            print(" PLAYER BUSTED SO DEALER WINS ")
                            game.updatePlayerAmount(bet * -1)
                            break
                    elif choice == 2:
                        game.unfoldDealerCards()
                        utility.displayLine()
                        game.displayDetails()
                        dealer_total = game.getDealerTotal()
                        player_total = game.getPlayerTotal()
                        while dealer_total < 16 and dealer_total < player_total:
                            game.pickCardForDealer(False)
                            utility.displayLine()
                            game.displayDetails()
                            dealer_total = game.getDealerTotal()

                        utility.displayLine()
                        if game.isDealerBusted():
                            print(" PLAYER WON !!! ")
                            game.updatePlayerAmount( bet )
                        elif dealer_total == player_total:
                            print(" TIE !!! ")
                        elif dealer_total > player_total:
                            print(" PLAYER LOST THE GAME ")
                            game.updatePlayerAmount(bet * -1)
                        else:
                            print(" PLAYER WON !!! ")
                            game.updatePlayerAmount(bet)
                        break
                    else:
                        print(" Invalid Choice. ")
        else:
            print(" Bet Amount must be less than or equal to Player Amount")
    elif choice == 2:
        game.displayPlayerAmount()
    elif choice == 3:
        print(" Exit From Game ")
        break
    else:
        print(" Invalid Choice. Try Again")

utility.displayLine()