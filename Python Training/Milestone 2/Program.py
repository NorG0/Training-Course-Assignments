import random
import time
from collections import  Counter


class Deck:
    ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', ('J',11), ('Q',12), ('K',13), ('A',14))
    suits = ('♡', '⟡', '♤', '♣')
    def __init__(self,name):
        self.name = name

    def genCard(self,cards,len):
        if len(cards) == 2:
                card_gen = f"|{cards[0][0]}{cards[0][1]}| -- |**|"
                print(card_gen)
        else:
            for i in range(len):
                card_gen = f"|{cards[i][0]}-{cards[i][1]}|"
                print(card_gen, end=" ")

    RANKS = {str(r[0]) if isinstance(r, tuple) else r: r[1] if isinstance(r, tuple) else int(r) for r in ranks}

    def get_hand_rank(self,cards):
        values = sorted([self.RANKS[card[0]] for card in cards])  # Chuyển rank về số và sắp xếp
        suits_list = [card[1] for card in cards]  # Lấy danh sách chất
        value_counts = Counter(values)  # Đếm số lần xuất hiện của từng giá trị bài
        most_common = value_counts.most_common()  # Danh sách [(giá trị, số lần xuất hiện)]

        is_flush = len(set(suits_list)) == 1  # Kiểm tra Flush (cùng chất)
        is_straight = values == list(range(values[0], values[0] + 5))  # Kiểm tra Straight (liên tiếp)

        if is_flush and is_straight and values[-1] == 14:
            return "Royal Flush"
        if is_flush and is_straight:
            return "Straight Flush"
        if most_common[0][1] == 4:
            return "Four of a Kind"
        if most_common[0][1] == 3 and most_common[1][1] == 2:
            return "Full House"
        if is_flush:
            return "Flush"
        if is_straight:
            return "Straight"
        if most_common[0][1] == 3:
            return "Three of a Kind"
        if most_common[0][1] == 2 and most_common[1][1] == 2:
            return "Two Pair"
        if most_common[0][1] == 2:
            return "One Pair"
        return "High Card"


class Host:
    def __init__(self,name,Deck):
        self.name = name
        self.table = []
        self.defaultcard = []
        self.deck = Deck
        self.value = 0

    def addPlayer(self):
        while(1):
            try:
                name = input('Please enter player 1 name: ')
                money = input('Please deposit your money ')
                player1 = Player(name,money,card1=[],card2=[])
                self.table.append(player1)
                if self.table : break
            except:
                print("May you enter wrong name or money format")

        while(1):
            try:
                name = input('Please enter player 2 name: ')
                money = int(input('Please deposit your money '))
                player2 = Player(name,money,card1=[],card2=[])
                self.table.append(player2)
                if len(self.table) == 2: break
            except:
                print("May you enter wrong name or money format")

        return self.table

    def deal_card(self,table):
        for i in range(len(table)):
            self.table[i].cards.append((random.choice(self.deck.ranks),random.choice(self.deck.suits)))
            self.table[i].cards.append((random.choice(self.deck.ranks),random.choice(self.deck.suits)))
        return self.table

    def deal_gamecards(self):
        for i in range(5):
            self.defaultcard.append((random.choice(self.deck.ranks),random.choice(self.deck.suits)))
        return self.defaultcard


class Player:
    def __init__(self,name,money,card1,card2):
        self.name = name
        self.money = money
        self.cards = []

    def showFoldcard(self):
        print(f"|{self.cards[1][0]}{self.cards[1][1]}|")
        time.sleep(2)
        print("\033[A\033[K") ##clear last line on cmd

    def bet(self,amount):
        if amount == 'all' and self.money > 0:
            self.money -= self.money
        elif self.money > 0:
            self.money -= amount
        else:
            print("You run out of money")
            return 0
        print(f"Your bet/raise {amount}$. Money now is: {self.money}")
        return amount

    def check(self):
        print("You Check")
        return True

    def fold(self):
        print("You fold and Lost the game!!!!")





poker_deck = Deck("52 cards")
pocker_table = Host("Table 1",poker_deck)


##Play game
print("Welcome to Poker Versus")
table_players = pocker_table.addPlayer()
table_players = pocker_table.deal_card(table_players)
##Host deal 5 showing card
default_cards = pocker_table.deal_gamecards()
poker_deck.genCard(default_cards,3)

##Player Cards
print("\nPlayer 1 cards: ")
poker_deck.genCard(table_players[0].cards)
print("Player 2 cards: ")
poker_deck.genCard(table_players[1].cards)
p1 = False
p2 = False
cards = 3
##GAMEPLAY
while(1):
    try:
        p1_action = input("Do you want to 1.Check 2.Bet 3.Fold, enter one number")
        if p1_action == 1:
            p1 = table_players[0].check()
        elif p1_action == 2:
            amt = int(input("Enter your amount"))
            p1 = table_players[0].bet(amt)
        elif p1_action == 3:
            table_players[0].fold()
            break
    except:
        print("Please enter right options and input format")

    try:
        p2_action = input("Do you want to 1.Check 2.Bet 3.Fold, enter one number")
        if p2_action == 1:
            p2 = table_players[0].check()
        elif p2_action == 2:
            amt = int(input("Enter your amount"))
            p2 = table_players[0].bet(amt)
        elif p2_action == 3:
            table_players[0].fold()
            break
    except:
        print("Please enter right options and input format")

    #Check Players
    cards += 1
    if cards == 5:
        p1_rs = ''
        p2_rs = ''
        if p1 == p2 == True:
            poker_deck.genCard(default_cards,cards)
            p1_rs = poker_deck.get_hand_rank(default_cards.append(table_players[0].cards))
            p2_rs = poker_deck.get_hand_rank(default_cards.append(table_players[1].cards))
        elif p1 - p2 == 0:
            pocker_table.value = p1 + p2
            poker_deck.genCard(default_cards, cards)
            p1_rs = poker_deck.get_hand_rank(default_cards.append(table_players[0].cards))
            p2_rs = poker_deck.get_hand_rank(default_cards.append(table_players[1].cards))
        if p2 > p1:
            call = input("If player 1 want to call enter 'call', if not you lose")
            if call == 'call':
                table_players[0].bet(p2)
                pocker_table.value = p1+p2
                poker_deck.genCard(default_cards, cards)
                p1_rs = poker_deck.get_hand_rank(default_cards.append(table_players[0].cards))
                p2_rs = poker_deck.get_hand_rank(default_cards.append(table_players[1].cards))
        print(p1_rs,p2_rs)
    else:
        if p1 == p2 == True:
            poker_deck.genCard(default_cards,cards)
        elif p1 - p2 == 0:
            pocker_table.value = p1 + p2
            poker_deck.genCard(default_cards, cards)
        if p2 > p1:
            call = input("If player 1 want to call enter 'call', if not you lose")
            if call == 'call':
                table_players[0].bet(p2)
                pocker_table.value = p1+p2
                poker_deck.genCard(default_cards, cards)







# for item in table:
#     print(f"Player name: {item.name}, money: {item.money}, card: {item.card1}, {item.card2}")