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
    #eka_kortti=pakka[:5]
    return kasi1, kasi2, loput_kortit#, eka_kortti

def pakan_vahennys(pakka,poistettavat_kortit):
    poistetut_kortit=[]
    for card in poistettavat_kortit:
        if card in pakka:
            pakka.remove(card)
            poistetut_kortit.append(card)
        print(pakka)

        if poistetut_kortit:
            print(f"poistettiin{', '.join(poistetut_kortit)}kadesta")

def pakan_lisays(hand, remaining_cards):
    while len(hand) < 5 and remaining_cards:
        new_card = remaining_cards.pop(0)
        hand.append(new_card)
        print(f"Added {new_card} to the hand.")



    #else:
        #print("no ei löytyny nnjiitä korttjea")
    #return poistettavat_kortit
#def pakan_paivitys(deal_hands):
    

