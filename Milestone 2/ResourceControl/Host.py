import Deck
import Player
import random
class Host:
    def __init__(self,name,table,Deck):
        self.name = name
        self.table = table
        self.deck = Deck

    def addPlayer(self):
        for i in range(2):
            print("Please input player info, NAME and MONEY")
            try:
                player = input(Player)
                self.table.append(player)
            except:
                print("Wrong Player FORMAT")
        return self.table

    def deal_card(self,table):
        for i in range(len(table)):
            self.table[i].card[i+1] = (random.choice(self.deck.ranks),random.choice(self.deck.suits))

        return self.table
