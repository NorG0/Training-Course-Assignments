import random


class Deck:

    suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
    ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


    def __init__(self,name):
        self.name = name



    def Straight_rule_check(self,current_Card):
###Rule of Sanhr
        rule = ''
        count = 0
        for i in range(current_Card):
            if current_Card[i][0] + 1 == current_Card[i+1][0]:
                count+=1
                if count == 5: rule = 'Straight'
        return rule

    def genCard(self,rank,suit):
        card_gen = (f"*****\n"
                    f"* {suit} *\n"
                    f"* {rank} *\n"
                    f"*****")
        return card_gen







