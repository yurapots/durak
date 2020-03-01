#DURAK
import random

#11=jack, 12=queen, 13=king, 14=ace
#card vs card
card1=['clubs', 10]
card2=['hearts', 14]
#card1 attacks card2
#scenarios to beat card2:
#1) same suit and card1>card2
#2) card1 is a trump card and card2 is not
def cardvscard(card1, card2, trumpcard):
    suit1=card1[0]
    num1=card1[1]
    suit2=card2[0]
    num2=card2[1]
    if suit1==suit2 and num1>num2:
        return True
    elif suit1==trumpcard and not suit2==trumpcard:
        return True
    else:
        return False

def deal():
    deck=cards
    random.shuffle(deck)
    random12=random.sample(range(36), 12)
    pl1=[deck[random12[0]], deck[random12[1]], deck[random12[2]], deck[random12[3]],
    deck[random12[4]], deck[random12[5]]]
    pl2=[deck[random12[6]], deck[random12[7]], deck[random12[8]], deck[random12[9]],
    deck[random12[10]], deck[random12[11]]]
    return pl1, pl2

def pickTrumpCard():
    return random.choice(['hearts', 'spades', 'diamonds', 'clubs'])









































#card=[suit, number]
#numbers 6-14, 11 jack, 12 queen, 13 king, 14 ace

cards=[
['hearts',6],['hearts',7],['hearts',8],['hearts',9],['hearts',10],['hearts',11],['hearts',12],['hearts',13],['hearts',14],
['spades',6],['spades',7],['spades',8],['spades',9],['spades',10],['spades',11],['spades',12],['spades',13],['spades',14],
['diamonds',6],['diamonds',7],['diamonds',8],['diamonds',9],['diamonds',10],['diamonds',11],['diamonds',12],['diamonds',13],['diamonds',14],
['clubs',6],['clubs',7],['clubs',8],['clubs',9],['clubs',10],['clubs',11],['clubs',12],['clubs',13],['clubs',14]]






