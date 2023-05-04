import random

values = {"two" : 2 , "three":3 , "four":4 ,"five":5 ,"six":6,"seven":7, "eight":8,"nine":9,"ten":10,"jack":10,"queen":11,"king":12,"ace":14}
suits = ("Hearts", "Diamonds",'spades',"clubs")
ranks =("two", "three" ,"four","five","six", "seven","eight","nine","ten","jack","queen","king","ace")




class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f"{self.rank} of {self.suit} and value = {self.value}"

class Deck:

    def __init__(self):
        self.all_cards =[]

        for suit in suits:
            for rank in ranks:
                created_card= Card(suit,rank)

                self.all_cards.append(created_card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
# two_spades =Card("spades" , "two")

new_deck = Deck()
new_deck.shuffle()

# for card in new_deck.all_cards:
#     print(card)

my_card = new_deck.deal_one()
print(my_card)



# print(two_spades)/
# print(values[two_spades.rank])