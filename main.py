import math
import random
class Player:
    def __init__(self,name,deck):
        self.name=name
    def getName(self):
        return self.name
    def setDeck(self,deck):
        self.deck=deck
    def PlayTurn(self,board,card):
        board.setBoard(card)
class Board:
    def __init__(self,round,numPlayer,numCard):
        self.numCard=numCard
        self.maxRound=math.floor(self.numCard/(2*numPlayer))
        self.round=round
        self.maxCapacity=round * numPlayer
        self.board=[]
        self.globalDeck=self.resetGlobalDeck()
    def setBoard(self,card):
        if(self.board[-1]<card):
            self.board.append(card)
            return True
        else:
            return False
    def resetGlobalDeck(self):
        self.globalDeck=[]
        i = 1
        while i <= self.numCard:
            self.globalDeck.append(i)
            i += 1

def Play(board,listPlayers):
    while (board.setBoard and board.round<board.maxRound):
        #funcion repartir
        board.round+=1

def dealCards(board,round,listPlayers,numPlayer):
    i=1
    while i <= numPlayer:
        # Repartimos el número de cartas (aleatoriamente) según la ronda
        deck = []
        while len(deck) < round:
            dealtCard = board.globalDeck[random.randint(0,len(board.globalDeck))]
            board.globalDeck.remove(dealtCard)
            deck.append(dealtCard)
        listPlayers[i].setDeck(deck)
        i+=1
    board.resetGlobalDeck()