
#properties of the players
class Player:
    def __init__(self, hand = [], money = 100, points = 0):
        self.hand = []
        self.money = money
        self.points = points
    
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
        self.money = money
player_1 = Player()
computer_player = Player([], 999999999999999, 0)

# creating the deck of cards and stroing their values, then appending the keys to a list that can be shuffled and dealt from  
ace_value = 1
deck_dict = {'Ace of Hearts': ace_value, 'King of Hearts':10, 'Queen of Hearts':10, 'Jack of Hearts': 10, 'Ten of Hearts':10, 'Nine of Hearts': 9, 'Eight of Hearts':8, 'Seven of Hearts':7, 'Six of Hearts':6, 'Five of Hearts':5, 'Four of Hearts':4, 'Three of Hearts':3, 'Two of Hearts':2, 'Ace of Diamonds': ace_value, 'King of Diamonds':10, 'Queen of Diamonds':10, 'Jack of Diamonds': 10, 'Ten of Diamonds':10, 'Nine of Diamonds': 9, 'Eight of Diamonds':8, 'Seven of Diamonds':7, 'Six of Diamonds':6, 'Five of Diamonds':5, 'Four of Diamonds':4, 'Three of Diamonds':3, 'Two of Diamonds':2, 'Ace of Clubs': ace_value, 'King of Clubs':10, 'Queen of Clubs':10, 'Jack of Clubs': 10, 'Ten of Clubs':10, 'Nine of Clubs': 9, 'Eight of Clubs':8, 'Seven of Clubs':7, 'Six of Clubs':6, 'Five of Clubs':5, 'Four of Clubs':4, 'Three of Clubs':3, 'Two of Clubs':2, 'Ace of Spades': ace_value, 'King of Spades':10, 'Queen of Spades':10, 'Jack of Spades': 10, 'Ten of Spades':10, 'Nine of Spades': 9, 'Eight of Spades':8, 'Seven of Spades':7, 'Six of Spades':6, 'Five of Spades':5, 'Four of Spades':4, 'Three of Spades':3, 'Two of Spades':2}

deck_list = []
for key in deck_dict.keys():
    deck_list.append(key)

#deal cards
import random
def deal(Player, deck_list):
    dealt_card = random.choice(deck_list)
    Player.hand.append(dealt_card)
    deck_list.remove(dealt_card)
    return Player.get_hand()

#calculate points in hand

'''if (player_1.get_points() + 11) > 21:
    ace_value = 1
else:
    ace_value = 11

for key, value in deck_dict.items():
    if key in player_1.get_hand():'''
    

#once dealing function, point calc function, and player class logic are done:
#player places a bet, deal 2 cards to the player and the computer, calculate their points
#if the player wins, they win a prize equal to what they bet, if they get a 21, they win 1.5 * their initial bet, and if they tie, they get their money back without winning any new money
#initital bet, deal, bet again, hit or stay (until they stay), calculate points, declare winner, distribute money

print(f'money: ${player_1.get_money()}')
init_bet = int(input('place your bet'))
deal(player_1, deck_list)
deal(player_1, deck_list)
deal(computer_player, deck_list)
deal(computer_player, deck_list)
print(f'your hand: {player_1.get_hand()}')
print(f"dealer's hand: {computer_player.get_hand()}")
double_down_choice = input('would you like to double down? (y/n)')
if double_down_choice == 'y':
    double_down = init_bet
else:
    double_down = 0

#hit/stay logic
done = False
while not done:
    hit_stay = input('would you like to hit or stay?')
    if hit_stay == 'hit':
        deal(player_1, deck_list)
    elif hit_stay == 'stay':
        done = True
        pass
    else:
        print('invalid input')
    print(f'your hand: {player_1.get_hand()}')
    print(f"dealer's hand: {computer_player.get_hand()}")


#dealer logic. the dealer will always hit if their point total is 16 or lower

#determine the winner, and distribute money. still needs logic for 21s
'''player_points = point_calc(player_1)
comp_points = point_calc(computer_player)
if player_points > comp_points:
    player_1.set_money(player_1.get_money() + init_bet + double_down)
    print('you defeated!')
    print(f'money: ${player_1.get_money()}')
elif player_points < comp_points:
    player_1.set_money(player_1.get_money() - init_bet - double_down)
    print('you lost, better luck next time :()')
    print(f'money: ${player_1.get_money()}')
else:
    print("it's a tie")
    print(f'money: ${player_1.get_money()}')'''

