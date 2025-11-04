
#properties of the players
class Player:
    def __init__(self, hand, money, points):
        self.hand = []
        self.money = 100
        self.points = 0
    
    def get_points(self):
        return self.points
    def get_hand(self):
        return self.hand
    def get_money(self):
        return self.money
    
    def set_points(self, points):
        self.points = points
    def set_hand(self, hand):
        self.hand = hand
    def set_money(self, money):
        self.money = 0
player_1 = Player({}, 0, 0)

# creating the deck of cards and stroing their values, then appending the keys to a list that can be shuffled and dealt from  
ace_value = 1
deck_dict = {'Ace of Hearts': ace_value, 'King of Hearts':10, 'Queen of Hearts':10, 'Jack of Hearts': 10, 'Ten of Hearts':10, 'Nine of Hearts': 9, 'Eight of Hearts':8, 'Seven of Hearts':7, 'Six of Hearts':6, 'Five of Hearts':5, 'Four of Hearts':4, 'Three of Hearts':3, 'Two of Hearts':2, 'Ace of Diamonds': ace_value, 'King of Diamonds':10, 'Queen of Diamonds':10, 'Jack of Diamonds': 10, 'Ten of Diamonds':10, 'Nine of Diamonds': 9, 'Eight of Diamonds':8, 'Seven of Diamonds':7, 'Six of Diamonds':6, 'Five of Diamonds':5, 'Four of Diamonds':4, 'Three of Diamonds':3, 'Two of Diamonds':2, 'Ace of Clubs': ace_value, 'King of Clubs':10, 'Queen of Clubs':10, 'Jack of Clubs': 10, 'Ten of Clubs':10, 'Nine of Clubs': 9, 'Eight of Clubs':8, 'Seven of Clubs':7, 'Six of Clubs':6, 'Five of Clubs':5, 'Four of Clubs':4, 'Three of Clubs':3, 'Two of Clubs':2, 'Ace of Spades': ace_value, 'King of Spades':10, 'Queen of Spades':10, 'Jack of Spades': 10, 'Ten of Spades':10, 'Nine of Spades': 9, 'Eight of Spades':8, 'Seven of Spades':7, 'Six of Spades':6, 'Five of Spades':5, 'Four of Spades':4, 'Three of Spades':3, 'Two of Spades':2}

deck_list = []
for key in deck_dict.keys():
    deck_list.append(key)




#deal cards
import random

dealt_card = random.choice(deck_list)
player_1.hand.append(dealt_card)
for card in deck_list:
    if card == dealt_card:
        deck_list.remove(dealt_card)
print(player_1.get_hand())

#calculate points in hand

if (player_1.get_points() + 11) > 21:
    ace_value = 1
else:
    ace_value = 11

for key, value in deck_dict.items():
    if key in player_1.get_hand():
        
