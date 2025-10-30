#question 5
def hailstone_seq(n):
    output_list = []
    while n != 1:
        if n % 2 == 0:
            n/=2
        else:
           n = (n*3)+1
        output_list.append(n)
    return output_list

#question 9

def count(list_of_cards):
    points = 0
    for card in list_of_cards:
        temp_card = str(card)
        if temp_card in ["2",'3','4','5','6']:
            points += 1
        elif temp_card in ['10','j','q','k','a']:
            points -= 1
    return points

deck_1 = [5,9,10,3,'j','a',4,8,5]
deck_2 = ['a','a','k','q','q','j']



#querstion 19

def is_acronym(s,words):
    if len(s) != len(words):
        return False
    for i in range (0,len(words)):
        current_word = words[i]
        if word == " ":
            return False
    if s[i] != current_word[0]:
        for word in words:
            first_letter = word[0]
    return True






