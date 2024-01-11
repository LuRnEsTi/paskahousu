import random

def create_pakka():
    numerot = ['A','2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    maat = ['hertta','ruutu','risti','pata']
    pakka = [f"{suit}_{rank}" for rank in numerot for suit in maat]
    return pakka

def shuffle_pakka(pakka):
    random.shuffle(pakka)

def deal_hands(pakka):
    kasi1 = pakka[:5]
    kasi2 = pakka[5:10]
    loput_kortit=pakka[10:]
    eka_kortti=pakka[:5]
    return kasi1, kasi2, loput_kortit, eka_kortti


